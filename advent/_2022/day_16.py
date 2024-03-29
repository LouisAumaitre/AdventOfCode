from copy import copy
from time import time

from advent.input_reader import read_lines_with_separator


class Valve:
    def __init__(self, name, pressure, leads_to):
        self.name = name
        self.pressure = pressure
        self.open = False
        self._leads_to = leads_to
        self.leads_to = []
        self._dist_to: dict['Valve', int] = {}
        self.forbidden_links = set()

    def dist(self, v: 'Valve'):
        return self.__dist(v, set())

    def __dist(self, target: 'Valve', exclude: set['Valve']):
        if target in self._dist_to:
            return self._dist_to[target]
        if target in self.leads_to:
            self._dist_to[target] = 1
            return 1
        if target is self:
            return 0
        exclude.add(self)
        return min([*[v.__dist(target, exclude) for v in self.leads_to if v not in exclude], 1000]) + 1

    def __repr__(self):
        return f'{self.name} {self.pressure}p {"o" if self.open else "x"}'


valves = {
    line[1]: Valve(line[1], int(line[5]), line[10:])
    for line in read_lines_with_separator('../../input/2022/day_16', ' ')
}

for v in valves.values():
    v.leads_to = [valves[n] for n in v._leads_to]


AA = valves['AA']
value_valves = {v for v in valves.values() if v.pressure}


def get_best_path_value(start, remaining_time, remaining_valves: set):
    if not remaining_valves or remaining_time <= 1:
        return 0, ''
    best_result = 0
    best_path = ''
    for target in remaining_valves:
        if target in start.forbidden_links:
            continue
        time = remaining_time - start.dist(target)  # move to valve
        time -= 1  # open valve
        rem_valves = copy(remaining_valves)
        rem_valves.remove(target)
        # print(f'Open valve {target} with {remaining_time}m remaining: +{remaining_time * target.pressure}')
        result, path = get_best_path_value(target, time, rem_valves)
        if time * target.pressure + result > best_result:
            best_result = time * target.pressure + result
            best_path = '->' + target.name + path
            # print(f'found {best_path} of value {best_result} (starting at {start} with {remaining_time}m)')
    return best_result, best_path


# t = time()
# best_option, best_path = get_best_path_value(AA, 30, value_valves)
# print(f'Part 1: {best_option} ({round(time() - t, 1)}s) by doing {best_path}')  # 2119; 9s


def get_best_elephant_path_value(start, remaining_time, remaining_valves: set):
    if not remaining_valves or remaining_time <= 1:
        # elephant is done, what did I do?
        my_score, my_path = get_best_path_value(AA, 26, remaining_valves)
        return my_score, '//' + my_path
    best_result = 0
    best_path = ''
    for i, target in enumerate(remaining_valves):
        if target in start.forbidden_links:
            continue
        time = remaining_time - start.dist(target)  # move to valve
        time -= 1  # open valve
        rem_valves = copy(remaining_valves)
        rem_valves.remove(target)
        result, path = get_best_elephant_path_value(target, time, rem_valves)
        if time * target.pressure + result > best_result:
            best_result = time * target.pressure + result
            best_path = '->' + target.name + path
        if len(remaining_valves) == 15:
            print(f'-{round(i*100/15)}%-')
    # or option to stop:
    if remaining_time < 15:
        my_score, my_path = get_best_path_value(AA, 26, remaining_valves)
        if my_score > best_result:
            return my_score, '//' + my_path
    return best_result, best_path


# MANUAL IMPROVEMENTS:
for v in value_valves:
    for v_ in value_valves:
        if v is not v_ and v.dist(v_) > 20:
            v.forbidden_links.add(v_)

t = time()
best_option, best_path = get_best_path_value(AA, 30, value_valves)
print(f'Part 1\': {best_option} ({round(time() - t, 1)}s) by doing {best_path}')  # 2119?; 2.5s

t = time()
best_option, best_path = get_best_elephant_path_value(AA, 26, value_valves)
print(f'Part 2: {best_option} ({round(time() - t, 1)}s) by doing {best_path}')  # 2562/2600+ is wrong

# for v in value_valves:
#     print(v)
#     for v_ in value_valves:
#         if v_ is not v and v.dist(v_) > 20 and v_ not in v.forbidden_links:
#             print(f'  - {v_} : {v.dist(v_)}')
