
def run_int_code(computer):
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
