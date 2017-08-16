empty = ()
numbers = (1, 2, 3)
mix = (1, 2, 'Three')

# empty = tuple()
# numbers = tuple(1, 2, 3)
# mix = tuple(1, 2, 'Three')

numbers1 = ([1, 2, 3])
# ([1, 2, 3])
numbers2 = tuple([1, 2, 3])
#(1, 2, 3)

numbers = (1, 2, 3)
sum = numbers + numbers
print(sum)

# strange usage
print(numbers * 2) #also (1, 2, 3, 1, 2, 3)

#access tuple
print(numbers[0]) #1
print(numbers[0:2]) #(1, 2)
print(numbers[0:3:2]) #(1, 3)

# support func
print(len(numbers)) # 3
print(min(numbers)) # 1
print(max(numbers)) # 3
print(3 in numbers) # true

#delete
numbers = (1, 2, 3)
del numbers
print(numbers) # NameError