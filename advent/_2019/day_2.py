import copy

from advent.input_reader import read_single_line_with_separator
from advent._2019.int_code import run_int_code

computer = read_single_line_with_separator('input/2019/day_2', ',', int)


def run_program(computer, noun, verb):
    computer[1] = noun
    computer[2] = verb
    run_int_code(computer)
    return computer[0]


print('PART 1')
print(run_program(computer, 12, 2))

print('PART 2')
desired_output = 19690720
base_memory = read_single_line_with_separator('input/2019/day_2', ',', int)
for i in range(0, 100):
    for j in range(0, 100):
        computer = copy.copy(base_memory)
        if run_program(computer, i, j) == desired_output:
            print(100 * i + j)
            break
