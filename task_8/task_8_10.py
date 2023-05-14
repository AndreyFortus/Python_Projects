def chess():
    coord = input('Input figure coordinates (example: d4): ')
    if 104 < ord(coord[0]) or 57 > ord(coord[0])\
            or 57 < ord(coord[1]) or 49 > ord(coord[1]):
        return 'Out of chess field'
    print(ord(coord[0]) + ord(coord[1]))
    color = 'black' if (ord(coord[0]) + ord(coord[1])) % 2 == 0 else 'white'
    return f'square is {color}'


print(chess())
