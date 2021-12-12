import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()
    lines = [line.rstrip() for line in lines]

close_to_open = {")":"(", "]":"[", "}":"{", ">":"<"}
openers = close_to_open.values()
closers = close_to_open.keys()

corrupt_closers = []
for i, line in enumerate(lines):
    print(i, '---------------------------------------------')
    opener_positions = {"(":[], "[":[], "{":[], "<":[]}
    line_copy = line

    idx = 0
    found_issue = False
    while 0 <= idx and idx < len(line_copy) and not found_issue:
        char = line_copy[idx]

        # store the positions of the opening characters
        if char in openers:
            for key in openers:
                if char == key:
                    opener_positions[key].append(idx)
                    idx += 1

        # find the last position of the matching opening character to remove
        else:
            print("\n", idx, line_copy)
            print("evaluating ", char, "at position ", idx)
            for val in closers:
                if char == val:
                    # find its partner and get last idx
                    try:
                        closest_opener_loc = opener_positions[close_to_open[val]][-1]
                    # IndexError means the list is empty so
                    # temporarily assign idx to trigger the else
                    except IndexError:
                        idx == -1

                    # remove the opener/close pair
                    if closest_opener_loc == (idx - 1):
                        print("removing positions ", closest_opener_loc, closest_opener_loc+1)
                        line_copy = line_copy[:closest_opener_loc] + line_copy[(closest_opener_loc+2):]
                        opener_positions[close_to_open[val]].pop()
                        idx -= 1

                    # if the last idx is not the previous idx, error
                    else:
                        print("the issue is: ", char, "\n")
                        corrupt_closers.append(char)
                        found_issue = True

closer_scores = {")":3, "]":57, "}":1197, ">":25137}
score_count = 0
for cc in corrupt_closers:
    score_count += closer_scores[cc]

print(score_count)

"""
I did this in an unnecessarily difficult way.
Regex simplifies things drastically, see:
https://github.com/mariothedog/advent-of-code/blob/main/2021/day10/day10.py

Otherwise, I didn't need to keep track of indexes by each opener.
I only needed to track the latest opener to verify that it matches the
earliest closer. Oh well. ¯\_( ") )_/¯
"""
