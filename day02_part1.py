import numpy as np

with open("input.txt") as f:
    lines = f.readlines()
    lines = [line.rstrip() for line in lines]

directions, values = zip( *[(x.split()[0], int(x.split()[1])) for x in lines] )
fwd_inds = [i for i, x in enumerate(directions) if x == 'forward']
dwn_inds = [i for i, x in enumerate(directions) if x == 'down']
upp_inds = [i for i, x in enumerate(directions) if x == 'up']

values = np.array(values)
fwd_values = values[fwd_inds]
dwn_values = values[dwn_inds]
upp_values = values[upp_inds]

fwd_sum = np.sum(fwd_values)
dwn_sum = np.sum(dwn_values)
upp_sum = np.sum(upp_values)
print(fwd_sum, dwn_sum-upp_sum)
