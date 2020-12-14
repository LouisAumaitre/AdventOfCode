from math import cos, sin, radians

from advent.input_reader import read_list_of_values

instructions = read_list_of_values('input/2020/day_12', str)

x = 0
y = 0
dir_x = 1
dir_y = 0
angle = 0
for i in instructions:
    order, val = i[0], int(i[1:])
    if order == 'N':
        y += val
    if order == 'S':
        y -= val
    if order == 'E':
        x += val
    if order == 'W':
        x -= val
    if order == 'F':
        x += dir_x * val
        y += dir_y * val
    if order == 'R':
        angle -= val
    if order == 'L':
        angle += val
    dir_x = int(cos(radians(angle)))
    dir_y = int(sin(radians(angle)))

print('Part 1')
print(abs(x)+abs(y))

ship_x, ship_y = 0, 0
way_x, way_y = 10, 1
for i in instructions:
    order, val = i[0], int(i[1:])
    if order == 'N':
        way_y += val
    elif order == 'S':
        way_y -= val
    elif order == 'E':
        way_x += val
    elif order == 'W':
        way_x -= val
    elif order == 'F':
        ship_x += way_x * val
        ship_y += way_y * val
    elif order == 'R':
        assert val % 90 == 0
        for i in range(val // 90):
            way_x, way_y = way_y, -way_x
    elif order == 'L':
        assert val % 90 == 0
        for i in range(val // 90):
            way_x, way_y = -way_y, way_x
    # print(f'{order}.{val}: ship({int(ship_x)};{int(ship_y)}) waypoint({int(way_x)};{int(way_y)})')

print('Part 2')
print(abs(ship_x)+abs(ship_y))
