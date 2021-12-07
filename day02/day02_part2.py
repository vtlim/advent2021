
with open("input.txt") as f:
    lines = f.readlines()
    lines = [line.rstrip() for line in lines]

depth, horiz, aim = 0, 0, 0
for l in lines:
    d = l.split()[0]
    v = int(l.split()[1])
    if d == 'down':
        aim += v
    if d == 'up':
        aim -= v
    if d == 'forward':
        horiz += v
        depth += (aim*v)
    print('depth: ', depth, '\thoriz: ', horiz, '\taim: ', aim)
print(horiz, depth, horiz*depth)
