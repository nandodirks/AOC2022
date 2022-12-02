import numpy as np

with open('AOC_2022_02/input.txt') as f:
    input = f.readlines()

play_values = {'X':1, 'Y':2, 'Z':3}
win_pairs = {'A':'Y', 'B':'Z', 'C':'X'}
tie_pairs = {'A':'X', 'B':'Y', 'C':'Z'}

total_score = 0
for game in input:
    parsed_game = game.split()
    play_score = play_values[parsed_game[1]]
    total_score += play_score

    win_condition = win_pairs[parsed_game[0]] == parsed_game[1]
    if win_condition:
        total_score += 6
    elif tie_pairs[parsed_game[0]] == parsed_game[1]:
        total_score += 3
