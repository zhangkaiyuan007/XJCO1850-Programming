x = [3, 1, 4, 1, 5]

result_sort = x.sort()
print(x)           # x is now sorted: [1, 1, 3, 4, 5]
print(result_sort) # None

y = [3, 1, 4, 1, 5]
result_sorted = sorted(y)
print(y)            # Original y unchanged: [3, 1, 4, 1, 5]
print(result_sorted) # New sorted list: [1, 1, 3, 4, 5]
