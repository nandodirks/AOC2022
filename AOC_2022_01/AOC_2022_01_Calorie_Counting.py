import numpy as np

with open('input.txt') as f:
    input = f.read()

elve_array = input.split('\n\n')

elve_sums = []
for i in elve_array:
    elve_contents = [int(j) for j in i.split('\n') if len(j) > 0]
    elve_total = sum(elve_contents)
    elve_sums += [elve_total]

max = np.max(elve_sums)