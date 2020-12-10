from advent.input_reader import read_list_of_values

cypher = read_list_of_values('input/2020/day_9', int)

pre = 25
inv = -1

print('Part 1')
for i in range(pre, len(cypher)):
    val = cypher[i]
    ok = False
    for n in cypher[i-pre:i]:
        for m in cypher[i-pre:i]:
            if n != m and n+m == val:
                ok = True
                break
        if ok:
            break
    if not ok:
        inv = val
        print(val)
        break

print('Part 2')

ok = False
for i, n in enumerate(cypher):
    # print(f'start at [{i}]: {n}')
    val = n
    for j, m in enumerate(cypher[i+1:]):
        val += m
        # print(f'sums to {val}')
        if val == inv:
            print(cypher[i:j + i + 2], sum(cypher[i:j + i + 2]))
            a = min(cypher[i:j + i + 2])
            b = max(cypher[i:j + i + 2])
            print(f'{a}+{b}={a+b}')
            ok = True
            break
        if val > inv:
            break
    if ok:
        break

print(sum(cypher[562:579]))