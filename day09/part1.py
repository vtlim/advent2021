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
answer_grid = tb_grid * lr_grid

counter = 0
for h, a in zip(heightmap, answer_grid):
    counter += np.sum(h[a] + 1)
print(counter)
