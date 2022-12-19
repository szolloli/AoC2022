buffer = """Monkey 0:
  Starting items: 61
  Operation: new = old * 11
  Test: divisible by 5
    If true: throw to monkey 7
    If false: throw to monkey 4

Monkey 1:
  Starting items: 76, 92, 53, 93, 79, 86, 81
  Operation: new = old + 4
  Test: divisible by 2
    If true: throw to monkey 2
    If false: throw to monkey 6

Monkey 2:
  Starting items: 91, 99
  Operation: new = old * 19
  Test: divisible by 13
    If true: throw to monkey 5
    If false: throw to monkey 0

Monkey 3:
  Starting items: 58, 67, 66
  Operation: new = old * old
  Test: divisible by 7
    If true: throw to monkey 6
    If false: throw to monkey 1

Monkey 4:
  Starting items: 94, 54, 62, 73
  Operation: new = old + 1
  Test: divisible by 19
    If true: throw to monkey 3
    If false: throw to monkey 7

Monkey 5:
  Starting items: 59, 95, 51, 58, 58
  Operation: new = old + 3
  Test: divisible by 11
    If true: throw to monkey 0
    If false: throw to monkey 4

Monkey 6:
  Starting items: 87, 69, 92, 56, 91, 93, 88, 73
  Operation: new = old + 8
  Test: divisible by 3
    If true: throw to monkey 5
    If false: throw to monkey 2

Monkey 7:
  Starting items: 71, 57, 86, 67, 96, 95
  Operation: new = old + 7
  Test: divisible by 17
    If true: throw to monkey 3
    If false: throw to monkey 1"""
class Monkey():
    def __init__(self, items = [], divisible = 0, i=0, e=0):
        self.items = items
        self.divisible = divisible
        self.i = i
        self.e = e
        self.counter = 0
    
    def resolveItem(self,monkeys,lcm):
        self.counter += 1
        if (len(self.items)):
            item = self.items.pop(0)
            itemScore = self.op(item)
            if ((itemScore % self.divisible)==0):
                monkeys[self.i].items.append(itemScore%lcm)
            else:
                monkeys[self.e].items.append(itemScore%lcm)
            
            
    def resolveAll(self,monkeys,lcm):
        while (len(self.items) != 0):
            self.resolveItem(monkeys,lcm)
            
    def addOp(self, op, number):
        if (op == '+'):
            if (number < 0):
                self.op = lambda x: x+x
            else:
                self.op = lambda x: x+number 
        else:
            if (number < 0):
                self.op = lambda x: x*x
            else:
                self.op = lambda x: x*number
monkey_in = buffer.split('\n\n')
monkeys = []
cm = 1
for monkey in monkey_in:
    monkey_lines = monkey.splitlines()
    items = list(map(int,monkey_lines[1].split(': ')[1].split(', ')))
    operator_in = monkey_lines[2].split('old ')[1]
    number =  -1 if operator_in.split(' ')[1] == 'old' else int(operator_in.split(' ')[1])
    divisible = int(monkey_lines[3].split('by ')[1])
    cm *= divisible
    i = int(monkey_lines[4].split()[-1])
    e = int(monkey_lines[5].split()[-1])
    new_monkey = Monkey(items,divisible,i,e)
    new_monkey.addOp(operator_in[0],number)
    
    monkeys.append(new_monkey)
    

for i in range(10000):
    
    for monkey in monkeys:
        monkey.resolveAll(monkeys, cm)

res = 1
monkeys.sort(key=lambda x: x.counter)
print(monkeys[-1].counter * monkeys[-2].counter)

        
        
