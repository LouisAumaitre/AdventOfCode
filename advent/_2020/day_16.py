fields_range = {}
your_ticket = []
nearby_tickets = []
value_validity = {}

with open('input/2020/day_16') as file:
    while True:
        line = file.readline()
        if len(line) == 1:
            break
        title, ranges = line.split(': ')
        range_a, range_b = ranges.split(' or ')
        a_1, a_2 = range_a.split('-')
        b_1, b_2 = range_b.split('-')
        fields_range[title] = (int(a_1), int(a_2), int(b_1), int(b_2))
    assert file.readline() == 'your ticket:\n'
    your_ticket = [int(i) for i in file.readline().split(',')]
    file.readline()
    assert file.readline() == 'nearby tickets:\n'
    line = file.readline()
    while line:
        nearby_tickets.append([int(i) for i in line.split(',')])
        line = file.readline()


def can_enter_at_least_one_field(value, fields):
    if value in value_validity:
        return value_validity[value]
    for a_1, a_2, b_1, b_2 in fields.values():
        if a_1 <= value <= a_2 or b_1 <= value <= b_2:
            value_validity[value] = True
            return True
    value_validity[value] = False
    return False


def get_error_rate(ticket, fields):
    error_rate = 0
    for entry in ticket:
        if not can_enter_at_least_one_field(entry, fields):
            error_rate += entry
    return error_rate


print('Part 1')
print(sum([get_error_rate(ticket, fields_range) for ticket in nearby_tickets]))

print('Part 2')
valid_tickets = [ticket for ticket in nearby_tickets if get_error_rate(ticket, fields_range) == 0]
print(f'{len(valid_tickets)} valid tickets')
field_possible_positions = {field: list(range(len(fields_range))) for field in fields_range.keys()}


def get_invalid_fields(value, fields):
    invalid_fields = []
    for field_name, (a_1, a_2, b_1, b_2) in fields.items():
        if not (a_1 <= value <= a_2 or b_1 <= value <= b_2):
            invalid_fields.append(field_name)
    assert len(invalid_fields) < len(fields), value
    return invalid_fields


for ticket in valid_tickets:
    for position, entry in enumerate(ticket):
        for invalid_field in get_invalid_fields(entry, fields_range):
            if position in field_possible_positions[invalid_field]:
                field_possible_positions[invalid_field].remove(position)

field_positions = {}
while field_possible_positions:
    defined = [field for field, possible_positions in field_possible_positions.items() if len(possible_positions) == 1]
    for field in defined:
        position, = field_possible_positions[field]
        field_positions[field] = position
        # print(f'{field} is at position {position}')
        del field_possible_positions[field]
        for remaining in field_possible_positions.values():
            if position in remaining:
                remaining.remove(position)

departure_keys = [
    field for field in field_positions.keys() if field.startswith('departure')
]
departure_value = 1
for departure_key in departure_keys:
    departure_value *= your_ticket[field_positions[departure_key]]
print(departure_value)
