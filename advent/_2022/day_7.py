from copy import copy
from typing import Union

from advent.input_reader import read_list_of_strings

data = read_list_of_strings('../../input/2022/day_7')

root = {}
parents = []
current = root

for line in data:
    if line[0:5] == '$ cd ':
        dir = line[5:]
        if dir == '/':
            current = root
        elif dir == '..':
            current = parents.pop()
        else:
            parents.append(current)
            current = current[dir]
    elif line == '$ ls':
        pass
    else:
        part1, part2 = line.split(' ')
        if part1 == 'dir' and part2 not in current:
            current[part2] = {}
        else:
            current[part2] = int(part1)


def partly_reduce(tree: Union[int, dict]):
    if isinstance(tree, int):
        return tree, 0
    total = 0
    mega_total = 0
    keys = set(tree.keys())
    for key in keys:
        value, sub_total = partly_reduce(tree[key])
        mega_total += sub_total
        if isinstance(value, int):
            tree[key] = value
            total += value
        else:
            total += 200000
    if total <= 100000:
        return total, mega_total + total
    return tree, mega_total


reduced_root, mega_total = partly_reduce(copy(root))

print(f'PART 1: {mega_total}')


def full_reduce(tree: Union[int, dict]):
    if isinstance(tree, int):
        return tree, []
    total = 0
    all_sizes = []
    keys = set(tree.keys())
    for key in keys:
        value, sizes = full_reduce(tree[key])
        all_sizes.extend(sizes)
        all_sizes.append(value)
        total += value
    return total, all_sizes


total_mem, sub_dirs = full_reduce(root)
missing_mem = 30000000 - (70000000 - total_mem)

candidates = [total for total in sub_dirs if total >= missing_mem]

print(f'PART 2: {min(candidates)}')
