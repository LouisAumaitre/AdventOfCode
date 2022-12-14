from advent.input_reader import read_lines_with_separator

input = read_lines_with_separator('../../input/2022/day_10', ' ', str)

cycle = 1
x = 1
total = 0
CRT = '#'


for instruction in input:
    if instruction is None:
        continue
    if len(instruction) == 1:
        assert instruction[0] == 'noop'
        cycle += 1
    if len(instruction) == 2:
        if instruction[1].startswith('-'):
            val = -int(instruction[1][1:])
        else:
            val = int(instruction[1])
        cycle += 1
        if cycle % 40 == 20:
            signal_strength = cycle * x
            total += signal_strength
            # print(signal_strength, cycle, x)
        if x <= cycle % 40 <= x + 2:
            CRT += '#'
        else:
            CRT += '.'
        cycle += 1
        x += val
    if cycle % 40 == 20:
        signal_strength = cycle * x
        total += signal_strength
        # print(signal_strength, cycle, x)
    if x <= cycle % 40 <= x + 2:
        CRT += '#'
    else:
        CRT += '.'

print(f'Part 1: {total}')
print('Part 2:')
for i in range(6):
    print(CRT[i * 40:i * 40 + 40])
