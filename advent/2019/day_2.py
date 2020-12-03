import copy

from advent.input_reader import read_single_line_with_separator

computer = read_single_line_with_separator('input/2019/day_2', ',', int)


def run_program(computer, noun, verb):
    head = 0
    computer[1] = noun
    computer[2] = verb
    while computer[head] != 99:
        if computer[head] == 1:
            computer[computer[head + 3]] = computer[computer[head + 1]] + computer[computer[head + 2]]
            head += 4
        elif computer[head] == 2:
            computer[computer[head + 3]] = computer[computer[head + 1]] * computer[computer[head + 2]]
            head += 4
        else:
            raise RuntimeError
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
