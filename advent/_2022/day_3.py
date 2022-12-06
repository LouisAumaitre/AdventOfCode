from advent.input_reader import read_list_of_strings

data = read_list_of_strings('../../input/2022/day_3')


def priority_of_rucksack(entry):
    entry = [*entry]
    part_1, part_2 = set(entry[:len(entry)//2]), set(entry[len(entry)//2:])
    error, = part_1.intersection(part_2)
    return priority(error)


def priority(item):
    if ord(item) >= ord('a'):
        return ord(item) - ord('a') + 1
    return ord(item) - ord('A') + 27


print(f'PART 1: {sum([priority_of_rucksack(entry) for entry in data])}')


def get_badge(sack_1, sack_2, sack_3):
    badge, = {*sack_1}.intersection({*sack_2}.intersection({*sack_3}))
    return priority(badge)


total = 0
for i in range(len(data) // 3):
    total += get_badge(data[3 * i], data[3 * i + 1], data[3 * i + 2])
print(f'PART 2: {total}')
