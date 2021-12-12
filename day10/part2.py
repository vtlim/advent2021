import sys
import statistics

with open(sys.argv[1]) as f:
    lines = f.readlines()
    lines = [line.rstrip() for line in lines]

open_to_close = {"(":")", "[":"]", "{":"}", "<":">"}
close_to_open = {")":"(", "]":"[", "}":"{", ">":"<"}
openers = close_to_open.values()
closers = close_to_open.keys()

noncorrupt = []
corrupt_closers = []
for i, line in enumerate(lines):
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
                        line_copy = line_copy[:closest_opener_loc] + line_copy[(closest_opener_loc+2):]
                        opener_positions[close_to_open[val]].pop()
                        idx -= 1

                    # if the last idx is not the previous idx, error
                    else:
                        corrupt_closers.append(char)
                        found_issue = True
    if not found_issue:
        noncorrupt.append(line_copy)

closer_scores = {")":1, "]":2, "}":3, ">":4}

all_scores = []
for line in noncorrupt:
    score = 0
    completer = ""
    for char in line[::-1]:
        close_char = open_to_close[char]
        completer += close_char
        score *= 5
        score += closer_scores[close_char]
    all_scores.append(score)

print(statistics.median(all_scores))
