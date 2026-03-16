''' setup '''
import random
nums = [ i for i in range(1000) ]
''' /setup '''


# options for random numbers:
print(random.randint(0,10000))
print(random.random())

# random data structure methods
print(nums[0:10])

random.shuffle(nums)
print(nums[0:10])

one_random = random.choice(nums)
print(one_random)

selection = random.choices(nums, k=10)
print(selection)


