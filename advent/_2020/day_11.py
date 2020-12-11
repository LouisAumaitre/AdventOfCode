from time import time

from advent.input_reader import read_map


def arrival(seats):
    new_seats = [
        [seat for seat in row] for row in seats
    ]
    for i, row in enumerate(seats):
        for j, seat in enumerate(row):
            if seat == '.':
                continue
            adjacent_seats = 0
            for x in range(max(0, i-1), min(i+2, len(seats))):
                for y in range(max(0, j-1), min(j+2, len(row))):
                    if i == x and j == y:
                        continue
                    adjacent_seats += int(seats[x][y] == '#')
            if seat == '#' and adjacent_seats >= 4:
                new_seats[i][j] = 'L'
            elif seat == 'L' and adjacent_seats == 0:
                new_seats[i][j] = '#'
    return new_seats


def to_str(seats):
    return ''.join([''.join(row) for row in seats])


def count_occupied(setup):
    return len(setup.replace('.', '').replace('L', ''))


print("Part 1")
setup = read_map('input/2020/day_11', {})
start = time()
current_setup = to_str(setup)
setup = arrival(setup)
new_setup = to_str(setup)
while current_setup != new_setup:
    current_setup = new_setup
    setup = arrival(setup)
    new_setup = to_str(setup)

print(time() - start)
print(count_occupied(new_setup))


def arrival_2(seats):
    new_seats = [
        [seat for seat in row] for row in seats
    ]
    for i, row in enumerate(seats):
        for j, seat in enumerate(row):
            if seat == '.':
                continue
            adjacent_seats = 0
            adjacent_seats += sees_occupied_in_direction(i, j, 1, 0, seats)
            adjacent_seats += sees_occupied_in_direction(i, j, 1, 1, seats)
            adjacent_seats += sees_occupied_in_direction(i, j, 0, 1, seats)
            adjacent_seats += sees_occupied_in_direction(i, j, -1, 1, seats)
            adjacent_seats += sees_occupied_in_direction(i, j, -1, 0, seats)
            adjacent_seats += sees_occupied_in_direction(i, j, -1, -1, seats)
            adjacent_seats += sees_occupied_in_direction(i, j, 0, -1, seats)
            adjacent_seats += sees_occupied_in_direction(i, j, 1, -1, seats)
            if seat == '#' and adjacent_seats >= 5:
                new_seats[i][j] = 'L'
            elif seat == 'L' and adjacent_seats == 0:
                new_seats[i][j] = '#'
    return new_seats


def sees_occupied_in_direction(start_x, start_y, x_diff, y_diff, seats):
    x = start_x + x_diff
    y = start_y + y_diff
    while 0 <= x <= len(seats) - 1 and 0 <= y <= len(seats[0]) - 1:
        seat = seats[x][y]
        if seat == 'L':
            return 0
        if seat == '#':
            return 1
        x += x_diff
        y += y_diff
    return 0


print("Part 2")
setup = read_map('input/2020/day_11', {})
start = time()
current_setup = to_str(setup)
setup = arrival_2(setup)
new_setup = to_str(setup)
while current_setup != new_setup:
    current_setup = new_setup
    setup = arrival_2(setup)
    new_setup = to_str(setup)

print(time() - start)
print(count_occupied(new_setup))
