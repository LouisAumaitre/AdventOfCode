from copy import copy
from time import time

input = [20, 9, 11, 0, 1, 2]


def memory_game(input, length):
    mem = copy(input)
    last_spoken = {nb: i for i, nb in enumerate(input)}
    del last_spoken[input[-1]]
    for i in range(len(input) - 1, length-1):
        last_nb = mem[i]
        new_nb = i - last_spoken.get(last_nb, i)
        last_spoken[last_nb] = i
        mem.append(new_nb)
    return mem[length-1]


print('Part 1')
print(memory_game([20, 9, 11, 0, 1, 2], 2020))
print('Part 2')
t = time()
print(memory_game([20, 9, 11, 0, 1, 2], 30000000), f'{time() - t}s')
