import collections

# read the input file
with open("day03.txt") as f:
    lines = f.readlines()
    lines = [line.rstrip() for line in lines]
copy_lines = lines.copy()
char_len = len(lines[0])

# -------------------------------------------
# calculate the oxygen generator rating
# -------------------------------------------
most = ''
for i in range(char_len):

    # if there's only number left, this is the answer
    if len(lines) == 1:
        most = lines[0]
        break

    # deconstruct the list of numbers by digit placement
    deconstruct = [l[i] for l in lines]

    # figure out the most/least common digit for placement i
    count1 = collections.Counter(deconstruct).most_common()[0][1]
    count2 = collections.Counter(deconstruct).most_common()[1][1]

    # if the count is the same, go with 1
    if count1 == count2:
        most += '1'

    # otherwise get the most common digit
    else:
        most += collections.Counter(deconstruct).most_common()[0][0]

    # trim the input list to remove non-relevant items
    for i, l in reversed(list(enumerate(lines))):
        if not l.startswith(most):
            lines.pop(i)

# -------------------------------------------
# calculate the co2 scrubber rating
# -------------------------------------------
lines = copy_lines.copy()
least = ''
for i in range(char_len):

    # if there's only number left, this is the answer
    if len(lines) == 1:
        least = lines[0]
        break

    # deconstruct the list of numbers by digit placement
    deconstruct = [l[i] for l in lines]

    # figure out the most/least common digit for placement i
    count1 = collections.Counter(deconstruct).most_common()[0][1]
    count2 = collections.Counter(deconstruct).most_common()[1][1]

    # if the count is the same, go with 0
    if count1 == count2:
        least += '0'

    # otherwise get the least common digit
    else:
        least += collections.Counter(deconstruct).most_common()[1][0]

    # trim the input list to remove non-relevant items
    for i, l in reversed(list(enumerate(lines))):
        if not l.startswith(least):
            lines.pop(i)

print(most, least)
print(int(most, 2), int(least, 2))
print(int(most, 2) * int(least, 2))

