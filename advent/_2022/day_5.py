filename = '../../input/2022/day_5'
stacks = [[] for i in range(10)]
instruct_mode = False
f = open(filename, mode='r')
for line in f:
    if instruct_mode:
        if line == '\n':
            pass
        _move, n, _from, origin, _to, destination = line[0:-1].split(' ')
        for i in range(int(n)):
            x = stacks[int(origin)].pop(0)
            stacks[int(destination)].insert(0, x)
    else:
        if line == '\n':
            instruct_mode = True
        elif line == ' 1   2   3   4   5   6   7   8   9\n':
            pass
        else:
            for i in range(1, 10):
                index = i * 4 - 3
                if index > len(line) or line[index] == ' ':
                    pass
                else:
                    stacks[i].append(line[index])

answer = ""
for stack in stacks:
    if stack:
        answer += stack[0]
print(f'PART 1: {answer}')


stacks = [[] for i in range(10)]
instruct_mode = False
f = open(filename, mode='r')
for line in f:
    if instruct_mode:
        if line == '\n':
            pass
        _move, n, _from, origin, _to, destination = line[0:-1].split(' ')
        moved = []
        for i in range(int(n)):
            x = stacks[int(origin)].pop(0)
            moved.insert(0, x)
        for i in range(int(n)):
            x = moved.pop(0)
            stacks[int(destination)].insert(0, x)
    else:
        if line == '\n':
            instruct_mode = True
        elif line == ' 1   2   3   4   5   6   7   8   9\n':
            pass
        else:
            for i in range(1, 10):
                index = i * 4 - 3
                if index > len(line) or line[index] == ' ':
                    pass
                else:
                    stacks[i].append(line[index])

answer = ""
for stack in stacks:
    if stack:
        answer += stack[0]
print(f'PART 2: {answer}')
