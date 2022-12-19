buffer = """noop
noop
addx 5
noop
noop
addx 1
addx 3
addx 2
addx 4
addx 3
noop
addx 2
addx 1
noop
noop
addx 4
noop
addx 1
addx 2
addx 5
addx 3
noop
addx -1
addx -37
addx 37
addx -34
addx 7
noop
addx -2
addx 2
noop
noop
noop
addx 5
addx 2
noop
addx 3
addx 15
addx -8
addx -9
addx 21
addx -9
addx 5
addx 2
addx 3
addx -2
addx -38
noop
addx 3
addx 37
addx -33
addx 5
noop
noop
addx 5
noop
noop
addx 5
noop
addx -1
addx 1
addx 5
noop
noop
addx 5
noop
noop
noop
addx 1
addx 2
noop
addx 3
addx -36
noop
noop
noop
addx 6
addx 21
addx -17
addx 18
addx -8
addx -7
addx 2
addx 5
addx -8
addx 13
addx -2
addx 7
noop
addx -2
addx 5
addx 2
addx 1
noop
addx -38
addx 4
addx 3
noop
addx 34
addx -29
addx -2
addx 10
addx -3
addx 2
addx 3
noop
addx -22
addx 2
addx 23
addx 7
noop
noop
addx 3
noop
addx 2
addx -18
addx 19
addx -38
addx 5
addx 2
noop
addx 1
addx 4
addx 1
noop
noop
addx 2
addx 5
addx 2
noop
addx 1
noop
addx 2
addx 8
addx -1
addx -30
addx 31
addx 2
addx 5
addx -35
noop"""

ops = buffer.splitlines()

q = []
s = 0
x = 1
i = 1

while len(ops):
    if ((i)%40 == 20):
        print()
        s += x*i
    if (len(q)):
        x += int(q.pop(0))
    else:
        o = ops.pop(0).split()
        if (o[0] != 'noop'):
            q.append(int(o[1]))
    i += 1
print(s)








ops = buffer.splitlines()

q = []
s = 0
x = 1
i = 0

lines = []
line = ''
while len(ops):
    if (abs(((i+1)%40) - x-1) <= 1):
        line += '#'
    else:
        line += '.'
        
    if ((i+1)%40 == 0):
        lines.append(line)
        line = ''
    if (len(q)):
        x += int(q.pop(0))
    else:
        o = ops.pop(0).split()
        if (o[0] != 'noop'):
            q.append(int(o[1]))
    i += 1
print('\n'.join(lines))



