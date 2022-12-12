from advent.input_reader import read_map

input = read_map('../../input/2022/day_12')


s_i, s_j, e_i, e_j = 0, 0, 0, 0
heights = []
paths = []
for i, line in enumerate(input):
    heights.append([])
    paths.append([])
    for j, c in enumerate(line):
        if c == 'S':
            heights[i].append(0)
            s_i, s_j = i, j
            paths[i].append(1000)
        elif c == 'E':
            heights[i].append(25)
            e_i, e_j = i, j
            paths[i].append(0)
        else:
            heights[i].append(ord(c) - ord('a'))
            paths[i].append(1000)


def print_map(height_map, path_map):
    print('-' * len(height_map[0]))
    for i, line in enumerate(path_map):
        s = ''
        for j, c in enumerate(line):
            if c == 1000:
                s += '.?.' + height_map[i][j]
            else:
                s += str(c).rjust(3) + height_map[i][j]
        print(s)


def create_path_map(position, height_map, path_map):
    i, j = position
    verbose = i == e_i + 5 and j == e_j + 3
    current_height = height_map[i][j]
    current_path = path_map[i][j]
    options = []
    around = []
    if i >= 0:
        south = height_map[i-1][j]
        if south >= current_height - 1 and path_map[i-1][j] > current_path + 1:
            path_map[i-1][j] = current_path + 1
            options.append((i-1, j))
        around.append((path_map[i-1][j], south))
    if i < len(height_map)-1:
        north = height_map[i+1][j]
        if north >= current_height - 1 and path_map[i+1][j] > current_path + 1:
            path_map[i+1][j] = current_path + 1
            options.append((i+1, j))
        around.append((path_map[i+1][j], north))
    if j >= 0:
        east = height_map[i][j-1]
        if east >= current_height - 1 and path_map[i][j-1] > current_path + 1:
            path_map[i][j-1] = current_path + 1
            options.append((i, j-1))
        around.append((path_map[i][j-1], east))
    if j < len(height_map[0])-1:
        west = height_map[i][j+1]
        if west >= current_height - 1 and path_map[i][j+1] > current_path + 1:
            path_map[i][j+1] = current_path + 1
            options.append((i, j+1))
        around.append((path_map[i][j+1], west))
    if verbose:
        print(position, current_path, current_height, around)
        print(options)
    for dir in options:
        create_path_map(dir, height_map, path_map)


create_path_map((e_i, e_j), heights, paths)
print_map(input, paths)
print(f'PART 1: {paths[s_i][s_j]}')  # 339

min_path_from_a = 339
for i, line in enumerate(paths):
    for j, path_length in enumerate(line):
        if input[i][j] == 'a':
            if path_length < min_path_from_a:
                min_path_from_a = path_length
print(f'PART 2: {min_path_from_a}')  # 332
