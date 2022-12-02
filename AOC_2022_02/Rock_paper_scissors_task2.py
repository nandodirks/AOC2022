import numpy as np

with open('AOC_2022_02/input.txt') as f:
    input = f.readlines()

play_values = {'X':1, 'Y':2, 'Z':3}
win_pairs = {'A':'Y', 'B':'Z', 'C':'X'}
tie_pairs = {'A':'X', 'B':'Y', 'C':'Z'}
loss_pairs = {'A':'Z', 'B':'X', 'C':'Y'}

total_score = 0
for game in input:
    parsed_game = game.split()
    if parsed_game[1] == 'X':
        pick = loss_pairs[parsed_game[0]]
        total_score += play_values[pick]

    elif parsed_game[1] == 'Y':
        pick = tie_pairs[parsed_game[0]]
        total_score += play_values[pick] + 3

    elif parsed_game[1] == 'Z':
        pick = win_pairs[parsed_game[0]]
        total_score += play_values[pick] + 6

