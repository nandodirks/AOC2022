

with open('AOC_2022_03/input.txt') as f:
    input = f.read().split()

def get_points(item_count):
    total = 0
    for key,val in item_count.items():
        if val > 1:
            print(points[key])
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
for rucksack in input:
    items = {}
    for i in range(len(rucksack)):
        if i < len(rucksack) / 2:
            try:
                items[rucksack[i]] = 1
            except:
                continue
        else:
            try:
                items[rucksack[i]] += 1
            except:
                continue
    total += get_points(items)

