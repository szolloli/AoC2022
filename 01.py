import sys
with open(sys.argv[1]) as f:
        lines = f.read()
sumList = sorted(list(map(lambda x: sum(list(map(int,x.splitlines()))),lines.split('\n\n'))))
print(sumList[-1])
print(sum(sumList[-3:]))
