from PIL import Image, ImageDraw

from advent.input_reader import read_lines_with_separator

OFFSET = 300

input = [
    [
        (int(pair.split(',')[0])-OFFSET, int(pair.split(',')[1]))
        for pair in line
    ]
    for line in read_lines_with_separator('../../input/2022/day_14', ' -> ', str)
]

cave = [
    [
        ' '
        for i in range(750-OFFSET)
    ]
    for j in range(183)
]


def sonar(cave_):
    s = ''
    for line in cave_:
        for c in line:
            s += c
        s += '\n'
    return s


def show_cave(cave_, rocks, id=0, show=False):
    scan = Image.new(mode='RGB', size=(len(cave_[0])*6, len(cave_)*16))
    d = ImageDraw.Draw(scan)
    d.text((1, 1), sonar(cave_), fill=(255, 255, 200))
    d.text((1, 1), rocks, fill=(150, 150, 255))
    if show:
        scan.show()
    scan.save(f'../../sand_{id}.png', 'png')
    # print(s)
    # print('-' * (535-OFFSET))


def draw_rocks(start, finish, cave_):
    s_i, s_j = start
    e_i, e_j = finish
    cave[s_j][s_i] = '#'
    if s_i == e_i and s_j < e_j:
        draw_rocks((s_i, s_j + 1), finish, cave_)
    elif s_i == e_i and s_j > e_j:
        draw_rocks((s_i, s_j - 1), finish, cave_)
    elif s_i < e_i and s_j == e_j:
        draw_rocks((s_i+1, s_j), finish, cave_)
    elif s_i > e_i and s_j == e_j:
        draw_rocks((s_i-1, s_j), finish, cave_)
    elif s_i == e_i and s_j == e_j:
        return
    else:
        raise ValueError(f'Cannot go from {start} to {finish}.')


for line in input:
    for i in range(len(line) - 1):
        draw_rocks(line[i], line[i+1], cave)
scan_rocks = sonar(cave)


def hourglass(cave_, until_hit_ground=True):
    i, j = 500-OFFSET, 0
    flowing = True
    while flowing and j < len(cave_)-1:
        if cave_[j+1][i] == ' ':
            j += 1
        elif cave[j+1][i-1] == ' ':
            i -= 1
            j += 1
        elif cave[j+1][i+1] == ' ':
            i += 1
            j += 1
        else:
            flowing = False
    cave_[j][i] = 'o'
    if until_hit_ground:
        return flowing
    else:
        return j == 0


pics = {10, 20, 30, 40, 50, 100, 200, 300, 400, 500, 1000, 2000, 3000, 5000, 10000, 20000}

sand = 0
while not hourglass(cave, until_hit_ground=True):
    sand += 1
    if sand in pics:
        show_cave(cave, scan_rocks, sand)


print(f'Part 1: {sand}')

sand += 2  # the one that dropped on the floor, and the final one
while not hourglass(cave, until_hit_ground=False):
    sand += 1
    if sand in pics:
        show_cave(cave, scan_rocks, sand)

show_cave(cave, scan_rocks, sand, True)
print(f'Part 2: {sand}')
