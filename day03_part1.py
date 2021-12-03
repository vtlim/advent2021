import collections

with open("day03.txt") as f:
    lines = f.readlines()
    lines = [line.rstrip() for line in lines]

char_len = len(lines[0])
deconstruct = ['' for i in range(char_len)]

for l in lines:
    for i in range(char_len):
        deconstruct[i] += l[i]

gamma = ''
epsilon = ''
for i in range(char_len):
    gamma += collections.Counter(deconstruct[i]).most_common()[0][0]
    epsilon += collections.Counter(deconstruct[i]).most_common()[1][0]

print(gamma, epsilon)
print(int(gamma, 2), int(epsilon, 2))
print(int(gamma, 2) * int(epsilon, 2))

