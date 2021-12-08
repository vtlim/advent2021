import numpy as np

with open("input.txt") as f:
    lines = f.readlines()[0].rstrip()
positions = np.sort([int(x) for x in lines.split(',')])

# calculate the average starting position
avg = np.mean(positions)

# determine if more starting positions are less or greater than avg
less_than = np.sum(positions < avg)
greater_than = np.sum(positions > avg)

# get range over which to consider
possibilities = np.arange(np.min(positions), np.max(positions)+1)

def calculate_fuel(ref, positions):
    counter = 0
    for p in positions:
        if p < ref: offset = 1
        else: offset = -1
        counter += sum(range(abs(ref-p+offset)))
    return counter

tracker = {}

# start on the high values
if greater_than > less_than:
    for p in np.flip(possibilities):
        if p not in tracker:
            tracker[p] = calculate_fuel(p, positions)

# start on the low values
else:
    for p in possibilities:
        if p not in tracker:
            tracker[p] = calculate_fuel(p, positions)

# find the position key with the lowest fuel value
min_key = min(tracker, key=tracker.get)
print(min_key, tracker[min_key])
