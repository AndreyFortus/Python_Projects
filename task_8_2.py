def figure(sides, figure_list):
    if 6 < sides or sides < 3:
        return 'for the correct operation of the program, the number of sides must be 3-6'
    else:
        for figure in range(len(figure_list)):
            if sides == figure + 3:
                return f'The figure with {sides} sides is {figure_list[figure]}'


figure_list = ['triangle', 'square', 'pentagon', 'hexagon']
number_of_sides = 3
print(figure(number_of_sides, figure_list))
