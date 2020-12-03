input_low, input_high = 236491, 713787


def check_valid(password):
    if int(password) < input_low or int(password) > input_high:
        return False
    for i in range(1, len(password)):
        if password[i-1] == password[i]:
            return True
    return False


def get_all_passwords_starting_with(start):
    if len(start) == 6:
        return [start]
    if start:
        last = int(start[-1])
    else:
        last = 1
    potential_passwords = []
    for i in range(last, 10):
        potential_passwords.extend(get_all_passwords_starting_with(start + str(i)))
    return potential_passwords


print('PART 1')
passwords = get_all_passwords_starting_with('')
print(len([password for password in passwords if check_valid(password)]))


def check_valid_2(password):
    if int(password) < input_low or int(password) > input_high:
        return False
    i = 1
    while i < len(password):
        if password[i-1] == password[i]:
            if i == len(password)-1 or password[i] != password[i+1]:
                return True
            else:
                key = password[i]
                while i < len(password) and password[i] == key:
                    i += 1
        else:
            i += 1
    return False


print('PART 2')
passwords = get_all_passwords_starting_with('')
print(len([password for password in passwords if check_valid_2(password)]))
