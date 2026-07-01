# Python Misc

A collection of useful Python syntax, pitfalls, and language features that frequently appear in coding interviews and competitive programming.

### Data Structures

```python
array = []

hashset = set()
hashset.add(val)
hashset.remove(val)

hashmap = {}
hashmap.get(key, default)

stack = []
stack.append(val)
stack.pop()
stack[-1]        # Peek

q = deque()
q.appendleft(val)
q.pop()

heap = []
heapq.heappush(heap, val)
smallest = heapq.heappop(heap)
heap[0]          # Peek smallest

heapq.heappush(heap, -val)
largest = -heapq.heappop(heap)
```

### Type Checking

```python
isinstance(x, int)
```

### Casting

String ↔ Integer
```python
index = ord(letter) - ord('a')
```

### Sorting

```python
nums.sort()
nums.sort(reverse=True)
sorted_nums = sorted(nums)   # returns new list

words.sort(key=len)
pairs.sort(key=lambda x: x[1])
pairs.sort(key=lambda x: (x[0], x[1]))
```

### Number Rounding

```python
round(x)
round(x, 2)      # keep 2 decimal places

import math

math.floor(x)
math.ceil(x)
math.trunc(x)
```

### Number Extremes

```python
float('inf')
-float('inf')
```

### List Multiplication Pitfall

❌ Wrong:

```python
grid = [[0] * n] * m
```

✅ Correct:

```python
grid = [[0] * n for _ in range(m)]
```

### defaultdict

```python
counter = defaultdict(int)
graph = defaultdict(list)
```

### nonlocal

nonlocal (or global) is only required when you reassign a variable name inside a nested function
