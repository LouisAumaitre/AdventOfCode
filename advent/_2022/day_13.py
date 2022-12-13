import functools

from advent.input_reader import read_eval

input = read_eval('../../input/2022/day_13')


def compare(a, b, depth=0):
    if isinstance(a, int) and isinstance(b, int):
        # print(' ' * depth + f'- compare {a} vs {b}')
        if a == b:
            return 0
        else:
            # if a < b:
            #     print(' ' * depth + f' - Left side smaller, right order')
            # else:
            #     print(' ' * depth + f' - Right side smaller, NOT right order')
            return b - a
    if isinstance(a, int):
        a = [a]
    if isinstance(b, int):
        b = [b]
    # print(' ' * depth + f'- compare {a} vs {b} (after conversion)')
    for i, e_a in enumerate(a):
        if i >= len(b):
            # print(' ' * depth + f' - Right side ran out, NOT right order')
            return -1
        result = compare(e_a, b[i], depth+1)
        if result != 0:
            return result
    if len(a) == len(b):
        if depth == 0:
            return 1
        return 0
    # print(' ' * depth + f' - Left side ran out, right order')
    return 1


total = 0
for i in range(len(input) // 3):
    # print(f'== Pair {i+1} ==')
    result = compare(input[i*3], input[i*3+1])
    if result >= 0:
        total += i + 1
    #     print(f' Current total = {total}')
    # print()

print(f'PART 1: {total}')

divider_a = [[2]]
divider_b = [[6]]

new_input = [_ for _ in input if _ is not None]
new_input.append(divider_a)
new_input.append(divider_b)

new_input = sorted(new_input, key=functools.cmp_to_key(compare), reverse=True)
index_factor = 1
for i, line in enumerate(new_input):
    if line == divider_b or line == divider_a:
        index_factor *= i + 1
    #     print(line, ' <-', i+1)
    # else:
    #     print(line)

print(f'Part 2: {index_factor}')
