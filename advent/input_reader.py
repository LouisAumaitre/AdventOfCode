def read_list_of_values(filename, value_type):
    # series of lines, with one value per line
    with open(filename) as file:
        return [value_type(line.replace('\n', '')) for line in file.readlines()]


def read_list_of_values_or_empty(filename, value_type):
    # series of lines, with one or zero value per line
    list_ = []
    f = open(filename, mode='r')
    for line in f:
        if line == '\n':
            list_.append(None)
        else:
            list_.append(value_type(line[0:-1]))
    return list_


def read_list_of_values_with_separators(filename, value_types, separator):
    # series of lines, with a fixed number of values per line
    with open(filename) as file:
        return [list(map(lambda ty, val: ty(val), value_types, line.replace('\n', '').split(separator))) for line in file.readlines()]


def read_translated_map(filename, code: dict):
    # series of lines, with each character representing a value
    with open(filename) as file:
        result = [
            list(map(lambda cr: code.get(cr, cr), line))
            for line in file.readlines()
        ]
        for i, line in enumerate(result):
            if line[-1] == '\n':
                result[i] = line[:-1]
        return result


def read_map(filename):
    # series of lines, with each character representing a value
    with open(filename) as file:
        result = [
            [*line.replace('\n', '')]
            for line in file.readlines()
        ]
        return result


def read_int_map(filename):
    # series of lines, with each character representing an int
    with open(filename) as file:
        result = [
            list(map(int, line.replace('\n', '')))
            for line in file.readlines()
        ]
        return result


def read_single_line_with_separator(filename, separator, value_type):
    # single line, with values separated by the same character
    with open(filename) as file:
        return list(map(value_type, file.readline().split(separator)))


def read_lines_with_separator(filename, separator, value_type):
    # multiple lines, with values separated by the same character
    with open(filename) as file:
        return [list(map(value_type, line.replace('\n', '').split(separator))) for line in file.readlines()]


def read_list_of_strings(filename):
    list_ = []
    f = open(filename, mode='r')
    for line in f:
        if line == '\n':
            list_.append(None)
        else:
            list_.append(line[0:-1])
    return list_


def read_eval(filename):
    list_ = []
    f = open(filename, mode='r')
    for line in f:
        if line == '\n':
            list_.append(None)
        else:
            list_.append(eval(line[0:-1]))
    return list_
