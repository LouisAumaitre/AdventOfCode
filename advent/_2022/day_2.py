from advent.input_reader import read_list_of_values_with_separators

data = read_list_of_values_with_separators('../../input/2022/day_2', [str, str], ' ')

hand_points = {'X': 1, 'Y': 2, 'Z': 3}
outcome = {
    'A': {'X': 3, 'Y': 6, 'Z': 0},
    'B': {'X': 0, 'Y': 3, 'Z': 6},
    'C': {'X': 6, 'Y': 0, 'Z': 3},
}


def total_score(input):
    score = 0
    for line in input:
        their_hand, my_hand = line
        hand_score = hand_points[my_hand]
        result = outcome[their_hand][my_hand]
        # print(their_hand, my_hand, hand_score, result)
        score += hand_score + result
    return score


print(f'EXPECTED SCORE: {total_score(data)}')

# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
true_outcome = {
    'A': {'X': 3, 'Y': 4, 'Z': 8},
    'B': {'X': 1, 'Y': 5, 'Z': 9},
    'C': {'X': 2, 'Y': 6, 'Z': 7},
}


def true_score(input):
    score = 0
    for line in input:
        their_hand, the_score = line
        score += true_outcome[their_hand][the_score]
    return score


print(f'TRUE SCORE: {true_score(data)}')
