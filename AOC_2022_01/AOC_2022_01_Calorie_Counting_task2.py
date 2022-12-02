import numpy as np

with open('AOC_2022_01/input.txt') as f:
    input = f.read()

elf_array = input.split('\n\n')

elf_sums = []
for i in elf_array:
    elf_contents = [int(j) for j in i.split('\n') if len(j) > 0]
    elf_total = sum(elf_contents)
    elf_sums += [elf_total]

max_elves = np.argpartition(elf_sums, -3)[-3:]
sum_max_elves = np.sum(np.array(elf_sums)[max_elves])