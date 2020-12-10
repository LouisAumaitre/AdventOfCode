from advent.input_reader import read_list_of_values

adapters = read_list_of_values('input/2020/day_10', int)

adapters = [0] + sorted(adapters)
adapters.append(adapters[-1]+3)

one_jolt = 0
three_jolt = 0

for i in range(1, len(adapters)):
    diff = adapters[i] - adapters[i-1]
    if diff == 1:
        one_jolt += 1
    if diff == 3:
        three_jolt += 1
    assert 0 < diff < 4

print('Part 1')
print(one_jolt, three_jolt, one_jolt * three_jolt)

combinations_so_far = 1
other_ways_to_get_to = {adapter: 0 for adapter in adapters}
for i in range(0, len(adapters)-1):
    value = adapters[i]
    if other_ways_to_get_to[value]:
        combinations_so_far += other_ways_to_get_to[value]
        # print(f'{combinations_so_far} ways to get to {value}')
        # assert combinations_so_far < 10000000000000
    if i == len(adapters)-1:
        break
    followers = adapters[i+1:i+4]
    assert len(followers) < 4
    followers = [f for f in followers if f < value + 4]
    if len(followers) == 1:
        continue
    # print(f'from {value}, can go to {followers} so far, {combinations_so_far} combinations)')
    for follower in followers[1:]:
        other_ways_to_get_to[follower] += combinations_so_far

print('Part 2')
print(combinations_so_far)
