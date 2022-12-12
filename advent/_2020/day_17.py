from copy import copy

from advent.input_reader import read_translated_map

cubes = read_translated_map('input/2020/day_17', {'#': True, '.': False})

active_cubes = {
    (x, y, 0) for x, line in enumerate(cubes) for y, cube in enumerate(line) if cube
}


def cycle(active_cubes):
    min_x, max_x = min([x for x, y, z in active_cubes]), max([x for x, y, z in active_cubes])
    min_y, max_y = min([y for x, y, z in active_cubes]), max([y for x, y, z in active_cubes])
    min_z, max_z = min([z for x, y, z in active_cubes]), max([z for x, y, z in active_cubes])
    next_cycle: set = copy(active_cubes)
    for x in range(min_x - 1, max_x + 2):
        for y in range(min_y - 1, max_y + 2):
            for z in range(min_z - 1, max_z + 2):
                neighbors = 0
                for i in (-1, 0, 1):
                    for j in (-1, 0, 1):
                        for k in (-1, 0, 1):
                            if i == j == k == 0:
                                continue
                            if (x+i, y+j, z+k) in active_cubes:
                                neighbors += 1
                if (x, y, z) in active_cubes:
                    if neighbors not in (2, 3):
                        next_cycle.remove((x, y, z))
                elif neighbors == 3:
                    next_cycle.add((x, y, z))
    return next_cycle


print('Part 1')
for i in range(6):
    active_cubes = cycle(active_cubes)
print(len(active_cubes))

active_cubes = {
    (x, y, 0, 0) for x, line in enumerate(cubes) for y, cube in enumerate(line) if cube
}


def hyper_cycle(active_cubes):
    min_x, max_x = min([x for x, y, z, w in active_cubes]), max([x for x, y, z, w in active_cubes])
    min_y, max_y = min([y for x, y, z, w in active_cubes]), max([y for x, y, z, w in active_cubes])
    min_z, max_z = min([z for x, y, z, w in active_cubes]), max([z for x, y, z, w in active_cubes])
    min_w, max_w = min([w for x, y, z, w in active_cubes]), max([w for x, y, z, w in active_cubes])
    next_cycle: set = copy(active_cubes)
    for x in range(min_x - 1, max_x + 2):
        for y in range(min_y - 1, max_y + 2):
            for z in range(min_z - 1, max_z + 2):
                for w in range(min_w - 1, max_w + 2):
                    neighbors = 0
                    for i in (-1, 0, 1):
                        for j in (-1, 0, 1):
                            for k in (-1, 0, 1):
                                for l in (-1, 0, 1):
                                    if i == j == k == l == 0:
                                        continue
                                    if (x+i, y+j, z+k, w+l) in active_cubes:
                                        neighbors += 1
                    if (x, y, z, w) in active_cubes:
                        if neighbors not in (2, 3):
                            next_cycle.remove((x, y, z, w))
                    elif neighbors == 3:
                        next_cycle.add((x, y, z, w))
    return next_cycle


print('Part 2')
for i in range(6):
    active_cubes = hyper_cycle(active_cubes)
print(len(active_cubes))
