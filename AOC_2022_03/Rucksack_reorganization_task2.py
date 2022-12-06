

with open('AOC_2022_03/input.txt') as f:
    input = f.read().split()

def get_points(item_count):
    total = 0
    for key,val in item_count.items():
        if val == 3:
            total += points[key]
    return total

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper_alphabet = [i.upper() for i in alphabet]

points = {}
for i in range(len(alphabet * 2)):
    if i <= 25:
        points[alphabet[i]] = i + 1
    else:
        points[upper_alphabet[i-26]] = i + 1

total = 0
for rucksack in range(3,len(input)+1, 3):
    elf_set = input[rucksack-3:rucksack]
    set_items = {}
    for elf_items in elf_set:
        for item in elf_items:
            if elf_items == elf_set[0]:
                try:
                    set_items[item] = 1
                except:
                    continue
            elif elf_items == elf_set[1]:
                try:
                    if set_items[item] == 1:
                        set_items[item] += 1
                except:
                    continue
            else:
                try:
                    if set_items[item] == 2:
                        set_items[item] += 1
                except:
                    continue
    total += get_points(set_items)



