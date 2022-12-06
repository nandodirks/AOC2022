with open('AOC_2022_05/input.txt') as f:
    input = f.readlines()

total_instr = []
parsed_box = []
for line in input:
    if line.startswith('move'):
        instructions = []
        for char in line.split():
            if char.isnumeric():
                instructions.append(char)
        total_instr.append(instructions)
    elif line.startswith('  ') or line.startswith('['):
        line_box = []
        for i in range(1, len(line), 4):
            line_box += line[i]
        parsed_box += [line_box]

stacks = []
for i in range(len(parsed_box[-1])):
    stack = []
    for row in parsed_box:
        try:
            if row[i] != ' ':
                stack += row[i]
        except:
            continue
    stacks += [stack]

for instruction in total_instr:
    number = int(instruction[0])
    source = int(instruction[1])-1
    dest = int(instruction[2])-1
    stacks[dest] = stacks[source][:number][::-1] + stacks[dest]
    stacks[source] = stacks[source][number:]

final_output = ''.join([i[0] for i in stacks])
print(final_output)