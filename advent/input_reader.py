def read_list_of_values(filename, value_type):
    with open(filename) as file:
        return [value_type(line) for line in file.readlines()]


def read_list_of_values_with_separators(filename, value_types, separator):
    with open(filename) as file:
        return [list(map(lambda ty, val: ty(val), value_types, line.split(separator))) for line in file.readlines()]


def read_map(filename, code: dict):
    with open(filename) as file:
        result = [
            list(map(lambda cr: code.get(cr, cr), line))
            for line in file.readlines()
        ]
        for i, line in enumerate(result):
            if line[-1] == '\n':
                result[i] = line[:-1]
        return result
