def figure(sides, figure_list):
    if 6 > sides or sides > 3:
        for i in range(len(figure_list)):
            if sides == i + 3:
                return f'The figure with {sides} sides is {figure_list[figure]}'
    return 'for the correct operation of the program, the number of sides must be 3-6'


list_figure = ['triangle', 'square', 'pentagon', 'hexagon']
print(figure(3, list_figure))
