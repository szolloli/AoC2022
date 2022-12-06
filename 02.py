strategy = input()

points = {
    'A':1,
    'B':2,
    'C':3,
    'X':1,
    'Y':2,
    'Z':3
}

results = {
    'A':{'X':3,'Y':6,'Z':0},
    'B':{'X':0,'Y':3,'Z':6},
    'C':{'X':6,'Y':0,'Z':3}
}

def foo(x):
    op, me = x.split(' ')
    return points[me] + results[op][me]

print(sum(list(map(foo,strategy.splitlines()))))

results2 = {
    'A':{'X':'Z','Y':'X','Z':'Y'},
    'B':{'X':'X','Y':'Y','Z':'Z'},
    'C':{'X':'Y','Y':'Z','Z':'X'}
}

def foo2(x):
    op, me = x.split(' ')
    return (points[me]-1)*3 + points[results2[op][me]]

print(sum(list(map(foo2,strategy.splitlines()))))
