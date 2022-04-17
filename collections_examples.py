from collections import Counter, namedtuple, OrderedDict, defaultdict , deque

#Counter

string = "abaaaabbbccc"

myCounter = Counter(string)
myCounter # Counter({'a': 3, 'b': 3, 'c': 3})
# function in counter: .items() .keys() .values() 

n = 2
# first slice will give most common variable in tuple, second slice give most common key 
myCounter.most_common(n)[0][0] # give the most common value with n as var

counterList = myCounter.elements() # will help you group the values and give an iterables to loop through
print(list(counterList)) #['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c']



# namedtuple
Point = namedtuple('Point', "x,y")
pt = Point(1,-4)
print(pt)
print(pt.x,pt.y) # 1 -4



ordered_Dict = OrderedDict()
ordered_Dict['A'] = 1
ordered_Dict['B'] = 2
ordered_Dict['C'] = 3
ordered_Dict['D'] = 4
ordered_Dict['E'] = 5
ordered_Dict
# OrderedDict([('A', 1), ('B', 2), ('C', 3), ('D', 4), ('E', 5)])

# default dict
default_Dict = defaultdict(int)
default_Dict['a'] = 1
default_Dict['b'] = 2
print(default_Dict['c']) #0

dep = [('Sales', 'John Doe'),
       ('Sales', 'Martin Smith'),
       ('Accounting', 'Jane Doe'),
       ('Marketing', 'Elizabeth Smith'),
       ('Marketing', 'Elizabeth Smith'),
       ('Marketing', 'Adam Doe'),
       ('Marketing', 'Adam Doe'),
       ('Marketing', 'Adam Doe')]

dep_dd = defaultdict(set)
for department, employee in dep:
    dep_dd[department].add(employee)

incomes = [('Books', 1250.00),
           ('Books', 1300.00),
           ('Books', 1420.00),
           ('Tutorials', 560.00),
           ('Tutorials', 630.00),
           ('Tutorials', 750.00),
           ('Courses', 2500.00),
           ('Courses', 2430.00),
           ('Courses', 2750.00),]

dd = defaultdict(float)
for product, income in incomes:
    dd[product] += income

for product, income in dd.items():
    print(f'Total income for {product}: ${income:,.2f}')

# deque
d = deque()
d.append(1)
d.append(2)

d.appendleft(3)
print(d) # deque([3, 1, 2])

d.extendleft([4,5,6])
print(d) # deque([6, 5, 4, 3, 1, 2])

d.rotate(2)
print(d) # deque([1, 2, 6, 5, 4, 3])

d.rotate(-1)
print(d) # deque([2, 6, 5, 4, 3, 1]) 