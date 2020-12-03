from advent.input_reader import read_list_of_values

modules = read_list_of_values('input/2019/day_1', int)

requirements = 0
for module in modules:
    module -= module % 3
    module /= 3
    module -= 2
    requirements += int(module)

print('PART 1')
print(requirements)


def need_fuel(mass):
    mass -= mass % 3
    mass /= 3
    mass -= 2
    if int(mass) <= 0:
        return 0
    return int(mass + need_fuel(mass))

requirements = 0
for module in modules:
    requirements += need_fuel(module)

print('PART 2')
print(requirements)
