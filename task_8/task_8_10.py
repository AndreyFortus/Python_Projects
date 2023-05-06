def chess():
    coord = input('Input figure coordinates (example: d4): ')
    if 104 < ord(coord[0]) or 57 > ord(coord[0])\
            or 57 < ord(coord[1]) or 49 > ord(coord[1]):
        return 'Out of chess field'
    if ord(coord[0]) % 2 == 1 and ord(coord[1]) % 2 == 1:
        return 'square is black'
    return 'square is white'


print(chess())
