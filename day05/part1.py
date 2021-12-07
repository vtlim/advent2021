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

for start, end in zip(start_coords, end_coords):

    # skip the ones not horizontal or vertical
    if (start[0] != end[0]) and (start[1] != end[1]):
        continue

    # build the path between start and end coordinates
    less_x = min(start[0], end[0])
    more_x = max(start[0], end[0]) + 1
    less_y = min(start[1], end[1])
    more_y = max(start[1], end[1]) + 1
    x_range = list(range(less_x, more_x, 1))
    y_range = list(range(less_y, more_y, 1))

    # loop over the cartesian product of the ranges
    for pair in itertools.product(x_range, y_range):
        tracker[pair[0], pair[1]] += 1

print(np.sum(tracker > 1))
