from advent.input_reader import read_lines_with_separator

wires = read_lines_with_separator('input/2019/day_3', ',', str)

wire_paths = []


for wire in wires:
    x, y = 0, 0
    horizontal_path = {}
    vertical_path = {}
    for instruction in wire:
        direction = instruction[0]
        amount = int(instruction[1:])
        if y not in horizontal_path:
            horizontal_path[y] = set()
        horizontal_path[y].add(x)
        if x not in vertical_path:
            vertical_path[x] = set()
        vertical_path[x].add(y)
        if direction == 'R':
            horizontal_path[y].update(range(x + 1, x + amount + 1))
            x += amount
        if direction == 'L':
            horizontal_path[y].update(range(x - amount, x))
            x -= amount
        if direction == 'D':
            vertical_path[x].update(range(y - amount, y))
            y -= amount
        if direction == 'U':
            vertical_path[x].update(range(y + 1, y + amount + 1))
            y += amount
    wire_paths.append((horizontal_path, vertical_path))


print('PART 1')
closest_intersection = -1
all_intersections = set()
red_wire_h, red_wire_v = wire_paths[0]
blue_wire_h, blue_wire_v = wire_paths[1]

for y, xes in red_wire_h.items():
    for x in xes:
        if y in blue_wire_v.get(x, []):
            new_intersection = abs(y) + abs(x)
            all_intersections.add((x, y))
            if new_intersection and (new_intersection < closest_intersection or closest_intersection == -1):
                closest_intersection = new_intersection
for x, yes in red_wire_v.items():
    for y in yes:
        if x in blue_wire_h.get(y, []):
            new_intersection = abs(y) + abs(x)
            all_intersections.add((x, y))
            if new_intersection and (new_intersection < closest_intersection or closest_intersection == -1):
                closest_intersection = new_intersection

print(closest_intersection)

print('PART 2')
total_steps_v = {}
total_steps_h = {}
for x, y in all_intersections:
    if x not in total_steps_v:
        total_steps_v[x] = {}
    if y not in total_steps_h:
        total_steps_h[y] = {}
    total_steps_v[x][y] = 0
    total_steps_h[y][x] = 0
for wire in wires:
    x, y = 0, 0
    steps = 0
    for instruction in wire:
        direction = instruction[0]
        amount = int(instruction[1:])
        if direction == 'R':
            if y in total_steps_h:
                for inter_x in total_steps_h[y]:
                    if x < inter_x <= x + amount:
                        total_steps_h[y][inter_x] += steps + inter_x - x
            x += amount
        if direction == 'L':
            if y in total_steps_h:
                for inter_x in total_steps_h[y]:
                    if x - amount <= inter_x < x:
                        total_steps_h[y][inter_x] += steps - inter_x + x
            x -= amount
        if direction == 'D':
            if x in total_steps_v:
                for inter_y in total_steps_v[x]:
                    if y - amount <= inter_y < y:
                        total_steps_v[x][inter_y] += steps - inter_y + y
            y -= amount
        if direction == 'U':
            if x in total_steps_v:
                for inter_y in total_steps_v[x]:
                    if y < inter_y <= y + amount:
                        total_steps_v[x][inter_y] += steps + inter_y - y
            y += amount
        steps += amount

total_per_intersection = [total_steps_v[x][y] + total_steps_h[y][x] for x, y in all_intersections if x or y]
print(min(total_per_intersection))
