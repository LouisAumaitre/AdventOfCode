from advent.input_reader import read_list_of_values

answers = read_list_of_values('input/2020/day_6', str)


def at_least_one_yes():
    total = 0
    current_group = set()
    for line in answers:
        if len(line) > 1:
            current_group.update(set(line[:-1]))
        else:
            total += len(current_group)
            current_group = set()
    total += len(current_group)
    return total


print('PART 1')
print(at_least_one_yes())


def all_yes():
    total = 0
    current_group = set(chr(i) for i in range(256))
    for line in answers:
        if len(line) > 1:
            current_group = current_group.intersection(set(line[:-1]))
        else:
            print(current_group, len(current_group))
            total += len(current_group)
            current_group = set(chr(i) for i in range(256))
    print(current_group, len(current_group))
    total += len(current_group)
    return total


print('PART 2')
print(all_yes())
