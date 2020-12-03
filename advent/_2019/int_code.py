def run_int_code_basic(computer):
    head = 0
    while computer[head] != 99:
        if computer[head] == 1:
            computer[computer[head + 3]] = computer[computer[head + 1]] + computer[computer[head + 2]]
            head += 4
        elif computer[head] == 2:
            computer[computer[head + 3]] = computer[computer[head + 1]] * computer[computer[head + 2]]
            head += 4
        else:
            raise RuntimeError


def run_int_code(computer, input_=None):
    head = 0
    while computer[head] != 99:
        opcode = computer[head] % 100
        mode = computer[head] // 100
        if opcode == 1:
            a = _get_first_parameter(computer, head, mode)
            b = _get_second_parameter(computer, head, mode)
            computer[computer[head + 3]] = a + b
            head += 4
        elif opcode == 2:
            a = _get_first_parameter(computer, head, mode)
            b = _get_second_parameter(computer, head, mode)
            computer[computer[head + 3]] = a * b
            head += 4
        elif opcode == 3:
            computer[computer[head + 1]] = input_
            head += 2
        elif opcode == 4:
            output = _get_first_parameter(computer, head, mode)
            print(f'output: {output}')
            head += 2
        elif opcode == 5:
            condition = _get_first_parameter(computer, head, mode)
            address = _get_second_parameter(computer, head, mode)
            head = address if condition else head + 3
        elif opcode == 6:
            condition = _get_first_parameter(computer, head, mode)
            address = _get_second_parameter(computer, head, mode)
            head = head + 3 if condition else address
        elif opcode == 7:
            a = _get_first_parameter(computer, head, mode)
            b = _get_second_parameter(computer, head, mode)
            computer[computer[head + 3]] = int(a < b)
            head += 4
        elif opcode == 8:
            a = _get_first_parameter(computer, head, mode)
            b = _get_second_parameter(computer, head, mode)
            computer[computer[head + 3]] = int(a == b)
            head += 4
        else:
            print(head, computer[head:head+5])
            raise RuntimeError(f'Unknown opcode {opcode}')


def _get_first_parameter(computer, head, mode):
    return computer[computer[head + 1]] if mode % 10 == 0 else computer[head + 1]


def _get_second_parameter(computer, head, mode):
    return computer[computer[head + 2]] if (mode // 10) % 10 == 0 else computer[head + 2]
