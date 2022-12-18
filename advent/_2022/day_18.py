from copy import copy

from advent.input_reader import read_list_of_values_with_separators

input = set(
    tuple(cube)
    for cube in read_list_of_values_with_separators('../../input/2022/day_18', [int, int, int], ',')
)


def count_exposed_sides(lava_droplet):
    exposed_sides = 0
    for x, y, z in lava_droplet:
        neighbors = [
            (x+1, y, z), (x, y+1, z), (x, y, z+1), (x-1, y, z), (x, y-1, z), (x, y, z-1),
        ]
        for n in neighbors:
            if n not in lava_droplet:
                exposed_sides += 1
    return exposed_sides


print(f'Part 1: {count_exposed_sides(input)}')

X = max(x for x, y, z in input)
Y = max(y for x, y, z in input)
Z = max(z for x, y, z in input)

water = set()
water.add((0, 0, 0))


def expand_water(pos, pond, lava):
    x, y, z = pos
    neighbors = [
        (x+1, y, z), (x, y+1, z), (x, y, z+1), (x-1, y, z), (x, y-1, z), (x, y, z-1),
    ]
    found = False
    for n in neighbors:
        n_x, n_y, n_z = n
        if n_x < 0 or n_y < 0 or n_z < 0 or n_x > X or n_y > Y or n_z > Z:
            continue
        if n not in lava and n not in pond:
            pond.add(n)
            found = True
    return found

stop = False
while not stop:
    found = False
    for drop in copy(water):
        found = expand_water(drop, water, input) or found
    if not found:
        stop = True
total_vol = (X+1) * (Y+1) * (Z+1)
water_vol = len(water)
lava_vol = len(input)
air_vol = total_vol - water_vol - lava_vol
print(
    f'{total_vol} cc {lava_vol} lava ({round(100*lava_vol/total_vol)}%) '
    f'{water_vol} water ({round(100*water_vol/total_vol)}%) '
    f'{air_vol} air ({round(100*air_vol/total_vol)}%)'
)
for x in range(X+1):
    for y in range(Y+1):
        for z in range(Z+1):
            filler = (x, y, z)
            if filler not in input and filler not in water:
                input.add(filler)


print(f'Part 2: {count_exposed_sides(input)}')
