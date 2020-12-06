from advent.input_reader import read_list_of_values

boarding_passes = read_list_of_values('input/2020/day_5', str)


def get_seat_number(code):
    row, column = 0, 0
    for i in range(0, 7):
        if code[i] == 'B':
            row += pow(2, 6-i)
    for i in range(0, 3):
        if code[i+7] == 'R':
            column += pow(2, 2-i)
    number = row * 8 + column
    return number


seats = sorted(map(get_seat_number, boarding_passes))
print('PART 1')
print(max(seats))

print('PART 2')
start = min(seats)
print(seats, start, start + len(seats))
for i, seat in enumerate(seats):
    if i+start != seat:
        print(seat)
        start += 1
        # break
