from advent.input_reader import read_lines_with_separator

input = read_lines_with_separator('../../input/2022/day_11', ' ', str)


monkey_by_id = {}
BIG_NB = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19


class Item:
    def __init__(self, value):
        self.factors = set()
        for i in [2, 3, 5, 7, 11, 13, 17, 19]:
            if value % i == 0:
                self.factors.add(i)
        self.value = value
        print(
            f'{value} is {self.factors}'
        )

    def times(self, mult):
        self.factors.add(mult)
        self.value *= mult

    def square(self):
        self.value *= self.value

    def add(self, val):
        self.value += val
        self.value %= BIG_NB
        self.factors = set()
        for i in [2, 3, 5, 7, 11, 13, 17, 19]:
            if self.value % i == 0:
                self.factors.add(i)


class Monkey:
    def __init__(self, id, items, operator, value, test, if_true, if_false):
        self.id = id
        self.items = items
        if operator == '+':
            self.operation = lambda x: x.add(value)
        elif value == 'old':
            self.operation = lambda x: x.square()
        else:
            self.operation = lambda x: x.times(value)
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.business = 0

    def play(self, family, worried):
        while self.items:
            self.examine(family, worried)

    def examine(self, family, worried):
        item = self.items.pop(0)
        self.operation(item)
        # if not worried:
        #     item = item // 3
        if self.test in item.factors:
            family[self.if_true].items.append(item)
        else:
            family[self.if_false].items.append(item)
        self.business += 1


for i in range(8):
    # use ints for part 1
    items = [Item(int(item.replace(',', ''))) for item in input[i * 7 + 1][4:]]
    operator = input[i * 7 + 2][-2]
    try:
        value = int(input[i * 7 + 2][-1])
    except ValueError:
        value = input[i * 7 + 2][-1]

    test = int(input[i * 7 + 3][-1])
    if_true = int(input[i * 7 + 4][-1])
    if_false = int(input[i * 7 + 5][-1])
    monkey_by_id[i] = Monkey(i, items, operator, value, test, if_true, if_false)


# for i in range(20):
#     # print(f'ROUND {i+1}')
#     for monkey in monkey_by_id.values():
#         monkey.play(monkey_by_id, False)


# business = [m.business for m in monkey_by_id.values()]
# business = sorted(business)
#
# print(f'PART 1: {business[-1] * business[-2]} ({business})')


for i in range(10000):
    if (i+1) % 100 == 0:
        print(f'ROUND {i+1}')
    for monkey in monkey_by_id.values():
        monkey.play(monkey_by_id, True)


business = [m.business for m in monkey_by_id.values()]
business = sorted(business)

print(f'PART 2: {business[-1] * business[-2]} ({business})')
