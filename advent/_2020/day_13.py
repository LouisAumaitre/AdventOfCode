import math

with open('input/2020/day_13') as file:
    depart = int(file.readline())
    buses = file.readline().split(',')

print('Part 1')
lines = [int(nb) for nb in buses if nb != 'x']
soonest_depart = 0
soonest_bus = 0
for bus in lines:
    missed_buses = depart // bus
    next_bus = (missed_buses + 1) * bus
    if not soonest_depart or next_bus < soonest_depart:
        soonest_depart = next_bus
        soonest_bus = bus

print(soonest_bus, soonest_depart, soonest_bus * (soonest_depart - depart))


def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)


print('Part 2')
depart_offset = {int(bus): i for i, bus in enumerate(buses) if bus != 'x'}
print(depart_offset)
current_depart = 0
jump = 41
for bus_nb in sorted(depart_offset.keys()):
    offset = depart_offset[bus_nb]
    while (current_depart + offset) % bus_nb != 0:
        current_depart += jump
    jump = lcm(jump, bus_nb)

for bus_nb, offset in depart_offset.items():
    assert (current_depart + offset) % bus_nb == 0, f't+{offset}mn: bus n°{bus_nb}'
print(current_depart)
