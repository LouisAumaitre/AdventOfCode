from advent.input_reader import read_list_of_values_or_empty

data = read_list_of_values_or_empty('../../input/2022/day_1', int)


elves = [0]
idx = 0

for x in data:
    if x is not None:
        elves[idx] += x
    else:
        idx += 1
        elves.append(0)

print(f'MAX: {max(elves)}')  # 71300

elves = sorted(elves)
print(f'TOP 3: {sum(elves[-3:])}')  # 209691
