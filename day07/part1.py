import numpy as np

with open("input.txt") as f:
    lines = f.readlines()[0].rstrip()
positions = np.sort([int(x) for x in lines.split(',')])

# calculate the average starting position
avg = np.mean(positions)

# determine if more starting positions are less or greater than avg
less_than = np.sum(positions < avg)
greater_than = np.sum(positions > avg)

def calculate_fuel(ref, positions):
    diffs = [abs(ref-x) for x in positions]
    return sum(diffs)

tracker = {}

# start on the high values
if greater_than > less_than:
    for p in np.flip(positions):
        if p not in tracker:
            tracker[p] = calculate_fuel(p, positions)

# start on the low values
else:
    for p in positions:
        if p not in tracker:
            tracker[p] = calculate_fuel(p, positions)

# find the position key with the lowest fuel value
min_key = min(tracker, key=tracker.get)
print(min_key, tracker[min_key])

"""
got lucky with the answer since I should have iterated for p
on the range of values from min position to max position
rather than on the existing original positions
"""
