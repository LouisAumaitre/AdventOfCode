from advent.input_reader import read_list_of_values_with_separators

input = read_list_of_values_with_separators('../../input/2022/day_9', [str, int], ' ')


class Knot:
    def __init__(self):
        self.i = 0
        self.j = 0
        self.known_positions = {(0, 0)}

    def move(self, dir):
        if dir == 'R':
            self.i += 1
        if dir == 'L':
            self.i -= 1
        if dir == 'U':
            self.j += 1
        if dir == 'D':
            self.j -= 1

    def follow(self, parent: 'Knot'):
        d = pow(abs(parent.j-self.j), 2) + pow(abs(parent.i-self.i), 2)
        if d > 2:
            if self.i == parent.i and self.j < parent.j - 1:
                self.j += 1
            elif self.i == parent.i and self.j > parent.j + 1:
                self.j -= 1
            elif self.j == parent.j and self.i < parent.i - 1:
                self.i += 1
            elif self.j == parent.j and self.i > parent.i + 1:
                self.i -= 1
            else:
                if self.i < parent.i:
                    self.i += 1
                else:
                    self.i -= 1
                if self.j < parent.j:
                    self.j += 1
                else:
                    self.j -= 1
            self.known_positions.add((self.i, self.j))

    def __repr__(self):
        return f'({self.i};{self.j}) [vis:{len(self.known_positions)}]'


map_t = [
    [
        0 for j in range(350)
    ]
    for i in range(300)
]
map_t[100][20] += 10


def print_map(map_):
    s_i, s_j, e_i, e_j = len(map_), len(map_[0]), 0, 0
    for i, line in enumerate(map_):
        for j, char in enumerate(line):
            if char > 0:
                s_i = min(s_i, i)
                e_i = max(e_i, i)
                s_j = min(s_j, j)
                e_j = max(e_j, j)
    # print(f'map from {s_i};{s_j} to {e_i};{e_j}')

    for i, line in enumerate(map_):
        if i < s_i or i > e_i:
            continue
        s = ''
        for j, char in enumerate(line):
            if s_j <= j <= e_j:
                s += '.' if char == 0 else ('#' if char > 9 else str(char))
        print(s)


def whip(input, rope_length):
    rope = []
    for _ in range(rope_length):
        rope.append(Knot())
    for dir, steps in input:
        for _ in range(steps):
            rope[0].move(dir)
            for i, knot in enumerate(rope[1:]):
                knot.follow(rope[i])
    return len(rope[-1].known_positions)


print(f'PART 1: {whip(input, 2)}')  # 6271
print(f'PART 2: {whip(input, 10)}')  # 2458
