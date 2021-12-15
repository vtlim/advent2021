import sys
import numpy as np

num_steps = 100
with open(sys.argv[1]) as f:
    lines = f.readlines()
    lines = [line.rstrip() for line in lines]

oct_levels = []

# organize the input lines into a matrix
for l in lines:
    oct_levels.append([int(x) for x in l])
oct_levels = np.array(oct_levels)

# function to track location of values greater than 9
def label_nines(oct_levels):
    where_nines = []
    for row in oct_levels:
        where_nines.append(row > 9)
    return np.array(where_nines)

# function to calculate number of True's adjacent to each position
def count_adjacent(where_true):
    board_size = len(where_true)
    num_adjacent = []

    for row_id in range(board_size):
        row_adjacent = []

        for col_id in range(board_size):
            cell_adjacent = 0

            # check top
            if (row_id > 0) and (where_true[row_id-1][col_id]):
                cell_adjacent += 1

            # check bottom
            if (row_id < board_size-1) and (where_true[row_id+1][col_id]):
                cell_adjacent += 1

            # check left
            if (col_id > 0) and (where_true[row_id][col_id-1]):
                cell_adjacent += 1

            # check right
            if (col_id < board_size-1) and (where_true[row_id][col_id+1]):
                cell_adjacent += 1

            # check top left diagonal
            if (row_id > 0) and (col_id > 0) and where_true[row_id-1][col_id-1]:
                cell_adjacent += 1

            # check top right diagonal
            if (row_id > 0) and (col_id < board_size-1) and where_true[row_id-1][col_id+1]:
                cell_adjacent += 1

            # check bottom left diagonal
            if (row_id < board_size-1) and (col_id > 0) and where_true[row_id+1][col_id-1]:
                cell_adjacent += 1

            # check bottom right diagonal
            if (row_id < board_size-1) and (col_id < board_size-1) and where_true[row_id+1][col_id+1]:
                cell_adjacent += 1

            row_adjacent.append(cell_adjacent)
        num_adjacent.append(np.array(row_adjacent))
    return np.array(num_adjacent)

flash_count = 0
# iterate over each step
for i in range(num_steps):

    # first increment the energy level of each position by 1
    oct_levels = oct_levels + 1

    # determine where the nines or higher values are
    where_nines = label_nines(oct_levels)

    # for each position, count the number of adjacent high values
    num_adjacent = count_adjacent(where_nines)

    # flash the octopuses, so set the high values to zero
    # then add the nearby energy levels
    # reset the original high values back to zero
    oct_levels[where_nines] = 0
    oct_levels = oct_levels + num_adjacent
    oct_levels[where_nines] = 0

    done_flashing = False
    while not done_flashing:

        # recheck for new flashers that were triggered by the last cycle
        # only allow an octopus to flash if it didn't already this round
        # relies on Boolean logic: true*false = false, true+false = true
        new_where_nines = label_nines(oct_levels)
        valid_new_where_nines = new_where_nines * np.invert(where_nines)
        where_nines = where_nines + valid_new_where_nines

        if valid_new_where_nines.sum() == 0:
            done_flashing = True
            continue

        num_adjacent = count_adjacent(valid_new_where_nines)
        oct_levels[where_nines] = 0
        oct_levels = oct_levels + num_adjacent
        oct_levels[where_nines] = 0
    flash_count += where_nines.sum()

print(oct_levels)
print(flash_count)
