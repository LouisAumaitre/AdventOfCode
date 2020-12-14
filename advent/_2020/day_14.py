from advent.input_reader import read_list_of_values_with_separators

code = read_list_of_values_with_separators('input/2020/day_14', (str, str), ' = ')


def apply_mask(unmasked_value, mask):
    for i, bit in enumerate(mask):
        expon = pow(2, 35 - i)
        if bit == 'X':
            continue
        before = unmasked_value // (expon * 2)
        after = unmasked_value % expon
        unmasked_value = before * expon * 2 + expon * int(bit) + after
    return unmasked_value


mem = {}
current_mask = 'X' * 36
for instruction, value in code:
    if instruction == 'mask':
        current_mask = value.replace('\n', '')
        continue
    address = int(instruction[4:-1])
    mem[address] = apply_mask(int(value), current_mask)

print('Part 1')
print(sum(mem.values()))


def apply_mask_2(address, mask):
    potential_addresses = [0]
    for i, bit in enumerate(mask):
        added_value = bit
        if bit == '0':
            expon = pow(2, 35 - i)
            added_value = str((address // expon) % 2)
        if added_value == '1':
            potential_addresses = [p_a * 2 + 1 for p_a in potential_addresses]
        elif added_value == '0':
            potential_addresses = [p_a * 2 for p_a in potential_addresses]
        else:
            new_addresses = []
            for p_a in potential_addresses:
                new_addresses.append(p_a * 2)
                new_addresses.append(p_a * 2 + 1)
            potential_addresses = new_addresses
    return potential_addresses


mem = {}
current_mask = '0' * 36
for instruction, value in code:
    if instruction == 'mask':
        current_mask = value.replace('\n', '')
        continue
    addresses = apply_mask_2(int(instruction[4:-1]), current_mask)
    value = int(value)
    for address in addresses:
        mem[address] = value

print('Part 2')
print(sum(mem.values()))
