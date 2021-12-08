import numpy as np

total_days = 80

with open("input.txt") as f:
    lines = f.readlines()[0].rstrip()
fishes = np.array([int(x) for x in lines.split(',')])

for i in range(total_days):

    # decrement the timers
    fishes = fishes - 1

    # check for negative values
    # checker is like [False False False  True False]
    checker = fishes < 0

    # reset the negative values to 6
    fishes[checker] = 6

    # add a new fish for every negative
    new_fishes = np.full(np.sum(checker), 8)
    fishes = np.concatenate((fishes, new_fishes))

print(np.shape(fishes)[0])
