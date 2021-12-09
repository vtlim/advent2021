import itertools
import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

# key is segment count and value is digit
uniq_seg_counts = {2: 1, 4: 4, 3: 7, 7: 8}

# actual letter in c_spot will help us distinguish the five-segment digits
c_spot = ""

answers = []
for l in lines:
    digits = [-1] * 10
    patterns, values = l.split(" | ")
    patterns = patterns.split()
    values = values.split()

    # calculate the number of segments found in each pattern
    lengths = [len(x) for x in patterns]

    # label the digits for the patterns we know
    for i, l in enumerate(lengths):
        if l in uniq_seg_counts.keys():
            digits[i] = uniq_seg_counts[l]

    # get the letters of digit 1 (2 segments) and digit 7 (3 segments)
    # and digit 4 (4 segments) to help determine identities of other digits
    twos_letters = set(patterns[lengths.index(2)])
    threes_letters = set(patterns[lengths.index(3)])
    fours_letters = set(patterns[lengths.index(4)])

    # -------------------------------------------
    # digits 0 6 9 each have six segments
    # -------------------------------------------
    six_indexes = lengths.index(6)
    six_indexes = [i for i, element in enumerate(lengths) if element == 6]

    for si in six_indexes:
        sixs_letters = set(patterns[si])

        # figure out which pattern goes to digit 6
        # the one that's digit 6 doesn't have twos_letters
        if not twos_letters.issubset(sixs_letters):
            digits[si] = 6

        # figure out which pattern goes to digit 9
        # the one that's digit 9 has digit 4 as a subset
        if fours_letters.issubset(sixs_letters):
            digits[si] = 9

        # the remaining one with six segments must be digit 0
        if twos_letters.issubset(sixs_letters) and not fours_letters.issubset(
            sixs_letters
        ):
            digits[si] = 0

    # -------------------------------------------
    # use digit 6 to figure out which is the c_spot
    # the letter in twos_letters not in digit6 letters is c_spot
    digit6_letters = set(patterns[digits.index(6)])
    leftover = twos_letters.difference(digit6_letters)
    c_spot = next(iter(leftover))

    # -------------------------------------------
    # digits 2 3 5 each have five segments
    # -------------------------------------------
    five_indexes = lengths.index(5)
    five_indexes = [i for i, element in enumerate(lengths) if element == 5]
    for si in five_indexes:
        fives_letters = set(patterns[si])

        # figure out which pattern goes to digit 3
        # the one that's digit 3 has all of twos_letters
        if twos_letters.issubset(fives_letters):
            digits[si] = 3

        # figure out which pattern goes to digit 5
        # the one that's digit 5 does NOT have the letter of c_spot
        if c_spot not in fives_letters:
            digits[si] = 5

    # the one that's left is digit 2
    digits[digits.index(-1)] = 2

    # -------------------------------------------

    # account for various orders to figure out which value is which digit
    permutations = []
    for p in patterns:
        permutations.append(["".join(x) for x in itertools.permutations(p)])
    for v in values:
        for i, rearrangements in enumerate(permutations):
            if v in rearrangements:
                answers.append(digits[i])
                continue

# join the answers into four digit numbers then sum
running_sum = 0
for i in range(0, len(answers), 4):
    mystring = "".join([str(x) for x in answers[i:i+4]])
    running_sum += int(mystring)
print(running_sum)
