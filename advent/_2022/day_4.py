from advent.input_reader import read_list_of_values_with_separators

data = read_list_of_values_with_separators('../../input/2022/day_4', [str, str], ',')


def contains(entry):
    elf_1, elf_2 = entry
    elf_1_start, elf_1_end = elf_1.split('-')
    elf_1_start, elf_1_end = int(elf_1_start), int(elf_1_end)
    elf_2_start, elf_2_end = elf_2.split('-')
    elf_2_start, elf_2_end = int(elf_2_start), int(elf_2_end)
    if elf_1_start <= elf_2_start and elf_2_end <= elf_1_end:
        return 1
    if elf_2_start <= elf_1_start and elf_1_end <= elf_2_end:
        return 1
    return 0


print(f'PART 1: {sum((contains(entry) for entry in data))}')


def overlap(entry):
    elf_1, elf_2 = entry
    elf_1_start, elf_1_end = elf_1.split('-')
    elf_1_start, elf_1_end = int(elf_1_start), int(elf_1_end)
    elf_2_start, elf_2_end = elf_2.split('-')
    elf_2_start, elf_2_end = int(elf_2_start), int(elf_2_end)
    if elf_1_start <= elf_2_start <= elf_1_end:
        return 1
    if elf_2_start <= elf_1_start <= elf_2_end:
        return 1
    return 0


print(f'PART 2: {sum((overlap(entry) for entry in data))}')
