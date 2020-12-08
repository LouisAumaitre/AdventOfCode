from copy import copy

from advent.input_reader import read_list_of_values_with_separators

code = read_list_of_values_with_separators('input/2020/day_8', [str, int], ' ')


def run_normally():
    has_run = [False] * len(code)
    i = 0
    acc = 0
    while 0 <= i < len(code):
        if has_run[i]:
            break
        has_run[i] = True
        ins, val = code[i]
        if ins == 'acc':
            acc += val
        if ins == 'jmp':
            i += val
        else:
            i += 1
    return acc


print('Part 1')
print(run_normally())

print('Part 2')
has_run = [False] * len(code)
fix_attempts = set()
address_of_last_fix = -1
visited_state_at_last_fix = None
head = 0
while head < len(code):
    if has_run[head]:  # loop
        print(f'found loop at {head}:{code[head]}, go back to {address_of_last_fix}')
        if head == -1:
            raise RuntimeError
        head = address_of_last_fix
        address_of_last_fix = -1
        has_run = visited_state_at_last_fix
        continue
    has_run[head] = True
    ins, val = code[head]
    if ins == 'acc':
        head += 1
    if ins == 'nop':
        if address_of_last_fix != -1 or head in fix_attempts:
            head += 1
            continue
        # try fix
        print(f'try fix at {head}, replacing nop w/ jmp')
        address_of_last_fix = head
        fix_attempts.add(head)
        visited_state_at_last_fix = copy(has_run)
        visited_state_at_last_fix[head] = False
        head += val
    if ins == 'jmp':
        if address_of_last_fix != -1 or head in fix_attempts:
            head += val
            continue
        # try fix
        print(f'try fix at {head}, replacing jmp w/ nop')
        address_of_last_fix = head
        fix_attempts.add(head)
        visited_state_at_last_fix = copy(has_run)
        visited_state_at_last_fix[head] = False
        head += 1

code[address_of_last_fix] = 'nop', 0
print(run_normally())
