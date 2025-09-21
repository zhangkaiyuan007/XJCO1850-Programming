import sys
from util import read_numbers

try:
  numbers = read_numbers()
  if not numbers:
    sys.exit("Error: no numbers provided")
except ValueError:
  sys.exit("Error: no numbers provided")

minimum = min(numbers)
print(f"Minimum = {minimum}")
maximum = max(numbers)
print(f"Maximum = {maximum}")
mean = sum(numbers) / len(numbers)
print(f"Mean    = {mean}")

def find_median(nums):
  nums_sorted = sorted(nums)
  n = len(nums_sorted)
  mid = n // 2
  if n % 2 == 1:
    return nums_sorted[mid]
  else:
    return (nums_sorted[mid - 1] + nums_sorted[mid]) / 2

median = find_median(numbers)
print(f"Median  = {median}")
