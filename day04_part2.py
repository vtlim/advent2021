import numpy as np

with open("day04.txt") as f:
    lines = f.readlines()
    lines = [line.rstrip() for line in lines]

# collect the list of bingo inputs
drawn = [int(x) for x in lines.pop(0).split(',')]

new_array = []
all_arrays = []
trackers = []

# organize the input lines into bingo matrices
for l in lines:
    if l == '':
        mylen = len(new_array)
        if mylen > 0:
            all_arrays.append(np.array(new_array))
            trackers.append(np.zeros((mylen, mylen)))
        new_array = []
        continue
    new_array.append([int(x) for x in l.split()])

# add the final array to the list
all_arrays.append(np.matrix(new_array))
trackers.append(np.zeros((mylen, mylen)))

found_last_winner = False
for d in drawn:
    for i, aa in enumerate(all_arrays):

        # look for the value d in aa
        search = np.where(aa==d)

        # if the value is found, mark it in the tracker as 1
        if search[0].size != 0:
            trackers[i][search[0], search[1]] = 1

    # check if any boards are winners
    for i, t in enumerate(trackers):
        column_sums = t.sum(axis=0)
        row_sums = t.sum(axis=1)
        if 5 in np.concatenate((column_sums, row_sums)):
            if len(all_arrays) > 1:
                all_arrays.pop(i)
                trackers.pop(i)
            else:
                winning_board = all_arrays[i]
                winning_tracker = t
                last_drawn = d
                found_last_winner = True
                break
    if found_last_winner:
        break

# convert the drawn numbers to zero and sum the rest
winning_tracker = winning_tracker.astype(bool)
winning_board[winning_tracker] = 0
print(np.sum(winning_board)*d)
