import operator
input = [l.strip() for l in open('day 11\input.txt').readlines()]
# items = [[] for y in range(7)]
op = {
    '+': lambda x, y: x + y, 
    '*': lambda x, y: x * y,}
monkeys = {}
items = []
mod = 1
for data in input:
    if data.startswith('Monkey'):
        monkey = data.split(" ")[1].split(":")[0]
        monkey = int(monkey)
    elif data.startswith('Starting'):
        nums = data.split(":")[1].split(",")
        for i in nums:
            # items[monkey].append(int(i))
            items.append(int(i))
    elif data.startswith('Operation'):
        index = data.find('+') if data.find('*') == -1 else data.find('*')
        operation = data[index]
        num = data.split(operation)[1].strip()
        num = int(num) if num.isnumeric() else 'old'
    elif data.startswith('Test:'):
        divided = data.split("by")[1].strip()
        divided = int(divided)
    elif data.startswith('If true:'):
        first_monkey = data.split("monkey")[1].strip()
        first_monkey = int(first_monkey)
    elif data.startswith('If false:'):
        second_monkey = data.split("monkey")[1].strip()
        second_monkey = int(second_monkey)
        monkeys[monkey] ={
            'items': items,
            'num': num,
            'divided': divided,
            'operation': operation, 
            'first_monkey': first_monkey,
            'second_monkey': second_monkey,
            'count': 0,
        }
        items = []
        mod *= divided
for i in range(10000):
    for monkey in monkeys:
        items = monkeys[monkey].get('items')
        operation = monkeys[monkey].get('operation')
        num = monkeys[monkey].get('num')
        divided = monkeys[monkey].get('divided')
        first_monkey = monkeys[monkey].get('first_monkey')
        second_monkey = monkeys[monkey].get('second_monkey')
        for item in items:
            new = op[operation](item, num) if type(num) == int else op[operation](item, item)
            # new //= 3 # PART  1
            new %= mod # PART 2
            if new % divided == 0:
                monkeys[first_monkey]['items'].append(new)
            else:
                monkeys[second_monkey]['items'].append(new)
            monkeys[monkey]['count'] += 1
        monkeys[monkey]['items'].clear()
biggest = []
for monkey in monkeys:
    biggest.append(monkeys[monkey]['count'])
biggest.sort()
print(biggest[-2] * biggest[-1])
