from advent.input_reader import read_lines_with_separator

beacon_sensor_pairs = [
    (int(line[3]), int(line[5]), int(line[11]), int(line[13]))
    for line in read_lines_with_separator('../../input/2022/day_15', ' ')
]

Y = 2000000


def read_sensor(pair, cave_):
    s_x, s_y, b_x, b_y = pair
    cave_[(s_x, s_y)] = 'S'
    cave_[(b_x, b_y)] = 'B'
    dist = abs(s_x-b_x) + abs(s_y-b_y)
    for x in range(s_x-dist, s_x+dist+1):
        if abs(s_x-x) + abs(s_y-Y) <= dist and (x, Y) not in cave_:
            cave_[(x, Y)] = '#'


cave = {}
for pair in beacon_sensor_pairs:
    read_sensor(pair, cave)

in_row = len([val for (x, y), val in cave.items() if y == Y and val == '#'])
print(f'Part 1: {in_row}')  # 5511201


def find_beacon(beacon_sensor_pairs, max_coordinate):
    found = set()
    for s_x, s_y, b_x, b_y in beacon_sensor_pairs:
        dist = abs(s_x-b_x) + abs(s_y-b_y)
        x, y = s_x - dist - 1, s_y
        # print(s_x, s_y, dist)
        for _ in range((dist + 1) * 4):
            if 0 <= x <= max_coordinate and 0 <= y <= max_coordinate and (x, y) not in found:
                if check_for_sensors(x, y, beacon_sensor_pairs):
                    found.add((x, y))
            # dist_now = abs(s_x-x) + abs(s_y-y)
            # print(x, y, dist_now)
            if x < s_x and y == s_y:
                x += 1
                y += 1
            elif x < s_x and y > s_y:
                x += 1
                y += 1
            elif x == s_x and y > s_y:
                x += 1
                y -= 1
            elif x > s_x and y > s_y:
                x += 1
                y -= 1
            elif x > s_x and y == s_y:
                x -= 1
                y -= 1
            elif x > s_x and y < s_y:
                x -= 1
                y -= 1
            elif x == s_x and y < s_y:
                x -= 1
                y += 1
            elif x < s_x and y < s_y:
                x -= 1
                y += 1
    return found


def check_for_sensors(x, y, beacon_sensor_pairs):
    for s_x, s_y, b_x, b_y in beacon_sensor_pairs:
        dist = abs(s_x-b_x) + abs(s_y-b_y)
        dist_now = abs(s_x-x) + abs(s_y-y)
        if dist_now <= dist:
            return False
    return True


found = find_beacon(beacon_sensor_pairs, 4000000)
print(found)
beacon, = found
tuning_frequency = beacon[0] * 4000000 + beacon[1]

print(f'Part 2: {tuning_frequency}')
