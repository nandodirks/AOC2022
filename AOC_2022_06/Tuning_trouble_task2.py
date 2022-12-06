with open('AOC_2022_06/input.txt') as f:
    input = f.readlines()

signal = input[0]

marker = ''
for i in range(0, len(signal)):
    if len(marker) == 14:
        total = ''
        for char in marker:
            if char not in total:
                total += char
        if len(total) == 14:
            print(i)
            break
        marker = marker[1:] + signal[i]
    else:
        marker = marker + signal[i]