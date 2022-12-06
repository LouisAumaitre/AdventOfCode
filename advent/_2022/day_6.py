from advent.input_reader import read_list_of_strings

data, = read_list_of_strings('../../input/2022/day_6')


def detect_buffer(length):
    buffer = [*data[:length-1]]
    for i in range(length-1, len(data)):
        input = data[i]
        if input in buffer or len(buffer) != len(set(buffer)):
            buffer.pop(0)
            buffer.append(input)
        else:
            # print(buffer, input)
            break
    return i + 1


print(f'PART 1: {detect_buffer(4)}')
print(f'PART 2: {detect_buffer(14)}')
