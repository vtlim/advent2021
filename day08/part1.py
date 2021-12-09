import sys
from collections import Counter

with open(sys.argv[1]) as f:
    lines = f.readlines()

all_counts = []
for l in lines:
    patterns, values = l.split(' | ')
    patterns = patterns.split()
    values = values.split()

    # calculate the number of segments found in each value
    value_lens = [len(x) for x in values]
    all_counts.append(value_lens)

# turn all_counts from 2D to 1D
all_counts = [item for sublist in all_counts for item in sublist]
counter = Counter(all_counts)
print(counter[2] + counter[4] + counter[3] + counter[7])

