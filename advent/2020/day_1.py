from advent.input_reader import read_list_of_values

report = read_list_of_values('input/2020/day_1', int)

report = sorted(report)


def find_sum(sub_report, total):
    index_a = 0
    index_b = len(sub_report) - 1
    while sub_report[index_a] + sub_report[index_b] != total:
        if sub_report[index_a] + sub_report[index_b] > total:
            index_b -= 1
        else:
            index_a += 1
        if index_a >= index_b:
            return None, None
    return index_a, index_b


a, b = find_sum(report, 2020)

print('PART 1')
print(report[a], report[b], report[a] + report[b], report[a] * report[b])

print('PART 2')
for i, value in enumerate(report):
    total_to_reach = 2020 - value
    a, b = find_sum(report[i + 1:], total_to_reach)
    if a != b:
        print(
            value, report[a + i + 1], report[b + i + 1],
            value + report[a + i + 1] + report[b + i + 1],
            value * report[a + i + 1] * report[b + i + 1],
        )
        break
