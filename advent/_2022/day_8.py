from advent.input_reader import read_int_map

data = read_int_map('../../input/2022/day_8')

w = len(data[0])
h = len(data)

visible = [
    [False for j in range(w)]
    for i in range(h)
]


def print_visible(map_):
    for i, line in enumerate(map_):
        output = ''
        for j, value in enumerate(line):
            if value:
                output += str(data[i][j])
            else:
                output += ' '
        print(output)


# W -> E
for i in range(h):
    highest_seen = -1
    for j in range(w):
        tree = data[i][j]
        if tree > highest_seen:
            visible[i][j] = True
            highest_seen = tree
# E -> W
for i in range(h):
    highest_seen = -1
    for j in reversed(range(w)):
        tree = data[i][j]
        if tree > highest_seen:
            visible[i][j] = True
            highest_seen = tree
# N -> S
for j in range(w):
    highest_seen = -1
    for i in range(h):
        tree = data[i][j]
        if tree > highest_seen:
            visible[i][j] = True
            highest_seen = tree
# N -> S
for j in range(w):
    highest_seen = -1
    for i in reversed(range(h)):
        tree = data[i][j]
        if tree > highest_seen:
            visible[i][j] = True
            highest_seen = tree

total = 0
for line in visible:
    for value in line:
        if value:
            total += 1

print(f'PART 1: {total}')


def scenic_score(trees, i, j):
    north, south, east, west = 1, 1, 1, 1
    treehouse = trees[i][j]
    x = i - 1
    while x >= 0 and trees[x][j] < treehouse:
        north += 1
        x -= 1
    x = i + 1
    while x < len(trees) and trees[x][j] < treehouse:
        south += 1
        x += 1
    y = j - 1
    while y >= 0 and trees[i][y] < treehouse:
        west += 1
        y -= 1
    y = j + 1
    while y < len(trees[0]) and trees[i][y] < treehouse:
        east += 1
        y += 1
    if north > i:
        north -= 1
    if south >= h - i:
        south -= 1
    if east >= w - j:
        east -= 1
    if west > j:
        west -= 1
    # if north * south * east * west > 1000:
    #     print(i, j, treehouse, north, south, west, east)
    return north * south * east * west


top_score = 0
for i in range(1, h - 1):
    for j in range(1, w - 1):
        score = scenic_score(data, i, j)
        if score > top_score:
            top_score = score

print(f'PART 2: {top_score}')


