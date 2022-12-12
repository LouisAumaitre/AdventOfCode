from advent.input_reader import read_translated_map

local_map = read_translated_map('input/2020/day_3', {'.': 0, '#': 1})


def how_many_trees(local_slope, start, vertical_value, horizontal_val):
    x = start
    y = 0
    trees = 0
    while y < len(local_slope):
        trees += local_slope[int(y)][int(x % len(local_slope[y]))]
        y += vertical_value
        x += horizontal_val
    return trees


print('PART 1')
print(how_many_trees(local_map, 0, 1, 3))

print('PART 2')
result = 1
for y, x in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]:
    print(x, y)
    new = how_many_trees(local_map, 0, y, x)
    result *= new
    print(new)
print(result)
