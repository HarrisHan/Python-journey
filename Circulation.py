# for
for num in range(1, 5):
    print(num)

for num in [1, 2, 3, 4, 5]:
    print(num)

user = {'email': 'aha@163.com', 'name': 'aha'}

for info in user:
    print(info)

for num in range(1, 5):
    print(num)
else:
    print('All numbers are iterated')

for num in range(1, 5):
    if num == 2:
        break
    print(num)
else:
    print('All numbers are iterated')

# while
num = 1

while num < 10:
    if num % 2 == 0:
        num += 1
        continue

    print(num)
    num += 1

