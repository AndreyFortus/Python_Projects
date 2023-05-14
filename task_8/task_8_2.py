LIST_FIGURES = ['triangle', 'square', 'pentagon', 'hexagon']


def figure(sides, figure_list):
    if 6 > sides or sides > 3:
        for i in range(len(figure_list)):
            if sides == i + 3:
                return f'The figure with {sides} sides is {figure_list[i]}'
    return 'for the correct operation of the program, the number of sides must be 3-6'


print(figure(3, LIST_FIGURES))
