from advent.input_reader import read_list_of_values

rules = read_list_of_values('input/2020/day_7', str)

print('Part 1')
can_contain_gold = {}
contained_by_colors = {}

for rule in rules:
    container, contained = rule.split(' contain ')
    container = container.replace(' bags', '')
    if contained.startswith('no other bags'):
        contained_by_colors[container] = set()
    else:
        containees = contained.replace(' bags', '').replace(' bag', '').replace('.', '').replace('\n', '').split(', ')
        contained_by_colors[container] = set([' '.join(bag.split(' ')[1:]) for bag in containees])


def can_contain_given_color(bag, given_color):
    if bag in can_contain_gold:
        return can_contain_gold[bag]
    if not contained_by_colors[bag]:
        can_contain_gold[bag] = False
        return False
    if given_color in contained_by_colors[bag]:
        can_contain_gold[bag] = True
        return True
    for sub_bag in contained_by_colors[bag]:
        if can_contain_given_color(sub_bag, given_color):
            can_contain_gold[bag] = True
            return True
    can_contain_gold[bag] = False
    return False


for color in contained_by_colors:
    can_contain_given_color(color, 'shiny gold')

print(len([color for color, can_contain in can_contain_gold.items() if can_contain]))

print('Part 2')
bag_sum_by_color = {}
contained_by_colors = {}

for rule in rules:
    container, contained = rule.split(' contain ')
    container = container.replace(' bags', '')
    if contained.startswith('no other bags'):
        contained_by_colors[container] = set()
    else:
        containees = contained.replace(' bags', '').replace(' bag', '').replace('.', '').replace('\n', '').split(', ')
        contained_by_colors[container] = [(int(bag.split(' ')[0]), ' '.join(bag.split(' ')[1:])) for bag in containees]


def total_bags_inside(bag):
    if bag in bag_sum_by_color:
        return bag_sum_by_color[bag]
    if not contained_by_colors[bag]:
        bag_sum_by_color[bag] = 0
        return 0
    total = 0
    for amount, sub_bag in contained_by_colors[bag]:
        total += total_bags_inside(sub_bag) * amount + amount
    bag_sum_by_color[bag] = total
    return total


print(total_bags_inside('shiny gold'))
