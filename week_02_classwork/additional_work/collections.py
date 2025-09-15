from collections import namedtuple, deque, Counter

Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)
print(p.x, p.y)  # Output: 3 4

dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print(dq)  # deque([0, 1, 2, 3, 4])

data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
count = Counter(data)
print(count)  # Counter({'apple': 3, 'banana': 2, 'orange': 1})
