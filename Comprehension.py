
# List comprehension
numbers = [i for i in range(1, 6)]
print(numbers)

# in math it like a {i | i belong to N, i>= 1, i<= 5}

numbers = [i for i in range(1, 6) if i % 2 == 0]
print(numbers)

strings = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
flatten = [int(i) for items in strings for i in items]
print(flatten) #[1, 2, 3, 4, 5, 6, 7, 8, 9]

xSamples = [2, 5, 8]
ySamples = [2, 6, 8]

points = [(x, y) for x in xSamples for y in ySamples if x != y]
print(points)

# Set comprehension
numberSet = {x for x in range(1, 6)}
print(numberSet)

# Dictionary comprehension
numberDict = {i: str(i) for i in range(1, 6)}
print(numberDict)

user = {'email': 'harris@link.com', 'workId': 13}
switch = {value: key for key, value in user.items()} #user.items() return a view object
print(switch)