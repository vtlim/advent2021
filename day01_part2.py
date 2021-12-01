
with open("input.txt") as f:
    lines = f.readlines()
    lines = [int(line.rstrip()) for line in lines]

length = range(len(lines)-2)
three_win = [(lines[x] + lines[x+1] + lines[x+2]) for x in length]

length = range(len(three_win))
subtract_previous = [(three_win[x] - three_win[x-1]) for x in length]

positives = [x for x in subtract_previous if x > 0]
print(len(positives))
