import numpy as np
import itertools

# read the input file
with open("input.txt") as f:
    lines = f.readlines()
    lines = [line.rstrip().split(' -> ') for line in lines]

# split lines into 2d array for each of start and end coordinates
start_coords = []
end_coords = []
for l in lines:
    start_coords.append( [ int(x) for x in l[0].split(',') ] )
    end_coords.append( [ int(x) for x in l[1].split(',') ] )
start_coords = np.array(start_coords)
end_coords = np.array(end_coords)

# determine the size of and set the tracker grid
start_x = start_coords[:,0]
start_y = start_coords[:,1]
end_x = end_coords[:,0]
end_y = end_coords[:,1]
max_x = np.max(np.concatenate((start_x, end_x))) + 1
max_y = np.max(np.concatenate((start_y, end_y))) + 1
tracker = np.zeros((max_x, max_y), dtype=int)

def build_range(val1, val2):
    ordered = False
    if val1 < val2:
        ordered = True
        smaller = val1
        bigger = val2 + 1
    else:
        smaller = val2
        bigger = val1 + 1
    myrange = list(range(smaller, bigger, 1))
    return myrange, ordered

def track_lines(x_range, y_range, tracker):
    # loop over the cartesian product of the ranges
    for pair in itertools.product(x_range, y_range):
        tracker[pair[0], pair[1]] += 1
    return tracker

for start, end in zip(start_coords, end_coords):

    # horizontal line
    if start[0] == end[0]:
        y_range, _ = build_range(start[1], end[1])
        tracker = track_lines([start[0]], y_range, tracker)

    # vertical line
    elif start[1] == end[1]:
        x_range, _ = build_range(start[0], end[0])
        tracker = track_lines(x_range, [start[1]], tracker)

    # diagonal line
    else:
        x_range, xordered = build_range(start[0], end[0])
        y_range, yordered = build_range(start[1], end[1])

        # order matters in building out the diagonal path
        if not xordered: x_range.reverse()
        if not yordered: y_range.reverse()
        for x, y in zip(x_range, y_range):
            tracker[x, y] += 1

print(np.sum(tracker > 1))
