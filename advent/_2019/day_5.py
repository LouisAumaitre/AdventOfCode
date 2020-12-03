from advent._2019.int_code import run_int_code
from advent.input_reader import read_single_line_with_separator

computer = read_single_line_with_separator('input/2019/day_5', ',', int)

print('PART 1')
run_int_code(computer, 1)

print('PART 2')
computer = read_single_line_with_separator('input/2019/day_5', ',', int)
run_int_code(computer, 5)
