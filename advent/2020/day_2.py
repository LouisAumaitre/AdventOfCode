from advent.input_reader import read_list_of_values_with_separators

passwords = read_list_of_values_with_separators('input/2020/day_2', [str, str, str], ' ')
formatted_passwords = []
for (amount, key, password) in passwords:
    min_amount, max_amount = map(int, amount.split('-'))
    key = key[:-1]  # remove :
    password = password[:-1]  # \n at the end
    formatted_passwords.append((min_amount, max_amount, key, password))

print('PART 1')
correct_passwords = 0
for (min_amount, max_amount, key, password) in formatted_passwords:
    count = 0
    for letter in password:
        if letter == key:
            count += 1
            if count > max_amount:
                break
    if min_amount <= count <= max_amount:
        correct_passwords += 1
print(correct_passwords)

print('PART 2')
correct_passwords = 0
for (first_index, second_index, key, password) in formatted_passwords:
    if (password[first_index-1] == key) != (password[second_index-1] == key):
        correct_passwords += 1
print(correct_passwords)
