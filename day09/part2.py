import sys
import numpy as np

with open(sys.argv[1]) as f:
    lines = f.readlines()

heightmap = []
for l in lines:
    separated = list(l.rstrip())
    separated = [int(x) for x in separated]
    heightmap.append(separated)

horiz_size = len(heightmap[0])
vert_size = len(heightmap)
print("hsize: ", horiz_size, "vsize: ", vert_size)
heightmap = np.array(heightmap)
heightmap_transposed = np.array(heightmap).transpose()

# first find the values which are lower than its left or right
# do this by taking two differences and comparing the True values
left_grid = []
right_grid = []
for i in range(horiz_size):
    if i==0:
        compare_to_right = (heightmap[:,i] - heightmap[:,i+1]) < 0
        right_grid.append(compare_to_right)
        left_grid.append([True]*vert_size)
    elif i==(horiz_size-1):
        compare_to_left = (heightmap[:,i] - heightmap[:,i-1]) < 0
        left_grid.append(compare_to_left)
        right_grid.append([True]*vert_size)
    else:
        compare_to_right = (heightmap[:,i] - heightmap[:,i+1]) < 0
        right_grid.append(compare_to_right)
        compare_to_left = (heightmap[:,i] - heightmap[:,i-1]) < 0
        left_grid.append(compare_to_left)

left_grid = np.array(left_grid).transpose()
right_grid = np.array(right_grid).transpose()
lr_grid = left_grid * right_grid

# now find values which are lower than its top and bottom
top_grid = []
bot_grid = []
for i in range(vert_size):
    if i==0:
        compare_to_bot = (heightmap_transposed[:,i] - heightmap_transposed[:,i+1]) < 0
        bot_grid.append(compare_to_bot)
        top_grid.append([True]*horiz_size)
    elif i==(vert_size-1):
        compare_to_top = (heightmap_transposed[:,i] - heightmap_transposed[:,i-1]) < 0
        top_grid.append(compare_to_top)
        bot_grid.append([True]*horiz_size)
    else:
        compare_to_bot = (heightmap_transposed[:,i] - heightmap_transposed[:,i+1]) < 0
        bot_grid.append(compare_to_bot)
        compare_to_top = (heightmap_transposed[:,i] - heightmap_transposed[:,i-1]) < 0
        top_grid.append(compare_to_top)

top_grid = np.array(top_grid)
bot_grid = np.array(bot_grid)
tb_grid = top_grid * bot_grid

# compare the left/right to the top/bottom to figure out low points
low_points = tb_grid * lr_grid

def check_4d(row_id, col_id, collector):

    # check top, if still in basin then go again
    if row_id > 0:
        top_val = heightmap[row_id-1][col_id]
        if (top_val < 9) and ((row_id-1, col_id) not in collector):
            collector.add((row_id-1, col_id))
            collector = check_4d(row_id-1, col_id, collector)

    # check bottom, if still in basin then go again
    if row_id < vert_size-1:
        bot_val = heightmap[row_id+1][col_id]
        if (bot_val < 9) and ((row_id+1,col_id) not in collector):
            collector.add((row_id+1,col_id))
            collector = check_4d(row_id+1, col_id, collector)

    # check left, if still in basin then go again
    if col_id > 0:
        left_val = heightmap[row_id][col_id-1]
        if (left_val < 9) and ((row_id,col_id-1) not in collector):
            collector.add((row_id,col_id-1))
            collector = check_4d(row_id, col_id-1, collector)

    # check right, if still in basin then go again
    if col_id < horiz_size-1:
        right_val = heightmap[row_id][col_id+1]
        if (right_val < 9) and ((row_id,col_id+1) not in collector):
            collector.add((row_id,col_id+1))
            collector = check_4d(row_id, col_id+1, collector)

    return collector

# find the basin size for every low point
all_basins = []

for row_id, (low_row, hm_row) in enumerate(zip(low_points, heightmap)):
    low_locs = np.where(low_row)[0]

    # no basins in this row
    if len(low_locs) == 0:
        continue

    for col_id in low_locs:
        print("starting eval of basin ", (row_id, col_id))

        # collector is a set of locations checked
        collector = {(row_id, col_id)}

        collector = check_4d(row_id, col_id, collector)
        all_basins.append(collector)

basin_sizes = [len(x) for x in all_basins]
basin_sizes.sort(reverse=True)
print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])
