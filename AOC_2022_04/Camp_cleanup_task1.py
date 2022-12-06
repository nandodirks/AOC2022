
with open('AOC_2022_04/input.txt') as f:
    input = f.read().split()

processed_assignments = []
for assignment_pair in input:
    split_pair = assignment_pair.split(',')
    processed_pair = []
    for assignment in split_pair:
        assignment_range = [int(i) for i in assignment.split('-')]
        processed_pair += [assignment_range]
    processed_assignments += [processed_pair]

total = 0
for pair in processed_assignments:
    if pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]:
        total += 1
        continue
    elif pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]:
        total += 1

