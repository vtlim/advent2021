import sys
import numpy as np

total_days = 256
tracker = (total_days + 1) * [0]

with open(sys.argv[1]) as f:
    lines = f.readlines()[0].rstrip()
fishes = [int(x) for x in lines.split(',')]
base_cnt = len(fishes)

for orig in fishes:

    # determine birthing dates for the original fish
    new_fish_by_orig = range(orig+1, total_days+1, 7)

    # increment the birthing date to count the new fish
    for day in new_fish_by_orig:
        tracker[day] += 1

# for the children of the original fish, figure out their children's births
for day, cnt in enumerate(tracker):
    if cnt > 0:
        new_children_days = range(day+9, total_days+1, 7)
        for nd in new_children_days:
            tracker[nd] += cnt

print(sum(tracker) + base_cnt)
