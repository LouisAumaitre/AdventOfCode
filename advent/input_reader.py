def read_list_of_values(filename, value_type):
    with open(filename) as file:
        return [value_type(line) for line in file.readlines()]


def read_list_of_values_with_separators(filename, value_types, separator):
    with open(filename) as file:
        return [list(map(lambda ty, val: ty(val), value_types, line.split(separator))) for line in file.readlines()]
