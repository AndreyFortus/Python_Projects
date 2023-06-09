import random
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.clock import Clock
from kivy.uix.label import CoreLabel


class GameWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)

        self._score_label = CoreLabel(text='Score: 0', font_size=20)
        self._score_label.refresh()
        self._score = 0

        self.register_event_type('on_frame')

        with self.canvas:
            Rectangle(source='recourses/background.jpg', pos=(0, 0), size=(Window.width, Window.height))
            self._score_instruction = Rectangle(texture=self._score_label.texture,
                                                pos=(70, Window.height - 20),
                                                size=self._score_label.texture.size)

        self.keysPressed = set()
        self._entities = set()

        Clock.schedule_interval(self._on_frame, 0)
        Clock.schedule_interval(self.spawn_enemies, 1)

    def spawn_enemies(self, dt):
        values_spawn = [55, 245, 450, 640]
        random_x = random.choice(values_spawn)
        y = Window.height

        random_speed = random.randint(100, 500)
        self.add_entity(Enemy((random_x, y), random_speed))

    def _on_frame(self, dt):
        self.dispatch('on_frame', dt)

    def on_frame(self, dt):
        pass

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value
        self._score_label.text = 'Score: ' + str(value)
        self._score_label.refresh()
        self._score_instruction.texture = self._score_label.texture
        self._score_instruction.size = self._score_label.texture.size

    def add_entity(self, entity):
        self._entities.add(entity)
        self.canvas.add(entity._instruction)

    def remove_entity(self, entity):
        if entity in self._entities:
            self._entities.remove(entity)
            self.canvas.remove(entity._instruction)

    def collides(self, e1, e2):
        r1x = e1.pos[0]
        r1y = e1.pos[1]
        r2x = e2.pos[0]
        r2y = e2.pos[1]
        r1w = e1.size[0]
        r1h = e1.size[1]
        r2w = e2.size[0]
        r2h = e2.size[1]

        return bool(r1x < r2x + r2w and r1x + r1w > r2x and r1y < r2y + r2h and r1y + r1h > r2y)

    def colliding_entities(self, entity):
        result = set()
        for e in self._entities:
            if self.collides(e, entity) and e != entity:
                result.add(e)
        return result

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard.unbind(on_key_up=self._on_key_up)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        self.keysPressed.add(keycode[1])

    def _on_key_up(self, keyboard, keycode):
        text = keycode[1]
        if text in self.keysPressed:
            self.keysPressed.remove(text)


class Entity(object):
    def __init__(self):
        self._pos = (0, 0)
        self._size = (150, 120)
        self._source = 'example.png'
        self._instruction = Rectangle(pos=self._pos, size=self._size, source=self._source)

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value):
        self._pos = value
        self._instruction.pos = self._pos

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
        self._instruction.size = self._size

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
        self._instruction.source = self._source


class Enemy(Entity):
    def __init__(self, pos, speed=100):
        super().__init__()
        self._speed = speed
        self.pos = pos
        self.size = (120, 170)
        self.source = 'recourses/enemy.png'
        game.bind(on_frame=self.move_step)

    def stop_callbacks(self):
        game.unbind(on_frame=self.move_step)

    def move_step(self, sender, dt):
        if self.pos[1] < 0:
            self.stop_callbacks()
            game.remove_entity(self)
            game.score += 10
            return
        for e in game.colliding_entities(self):
            if e == game.player:
                game.add_entity(Explosion(self.pos))
                self.stop_callbacks()
                game.remove_entity(self)
                game.score -= 100
                return

        step_size = self._speed * dt
        new_x = self.pos[0]
        new_y = self.pos[1] - step_size
        self.pos = (new_x, new_y)


class Explosion(Entity):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.source = 'recourses/explosion.png'
        Clock.schedule_once(self._remove_me, 1)

    def _remove_me(self, dt):
        game.remove_entity(self)


class Player(Entity):
    def __init__(self):
        super().__init__()
        self.source = 'recourses/car.png'
        game.bind(on_frame=self.move_step)
        self.pos = (400, 0)

    def stop_callback(self):
        game.unbind(on_frame=self.move_step)

    def move_step(self, sender, dt):
        step_size = 500 * dt
        newx = self.pos[0]
        newy = self.pos[1]
        if 'a' in game.keysPressed:
            newx -= step_size
        if 'd' in game.keysPressed:
            newx += step_size
        self.pos = (newx, newy)


game = GameWidget()
game.player = Player()
game.add_entity(game.player)


class MyApp(App):
    def build(self):
        return game


if __name__ == "__main__":
    app = MyApp().run()
