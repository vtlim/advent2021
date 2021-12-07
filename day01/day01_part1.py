
with open("input.txt") as f:
    lines = f.readlines()
    lines = [int(line.rstrip()) for line in lines]

length = range(len(lines))
subtract_previous = [(lines[x] - lines[x-1]) for x in length]

positives = [x for x in subtract_previous if x > 0]
print(len(positives))
