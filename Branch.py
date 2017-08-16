num = 2
if num < 10:
    content = '{0} is less than 10'.format(num)
    print(content)

# code must have a same indentation
num = 15
if num < 10:
    content = '{0} is less than 10'.format(num)
elif 10 < num < 20:
    print('between 10 and 20')
else:
    print('greater than or equal to 20')

# Boolean

if num < 10:
    content = '{0} is less than 10'.format(num)
    print(content)
elif num > 10 and num < 20:
    print('between 10 and 20')
elif num == 10 or num == 20:
    print('equal to 10 or 20')
elif not num == 10: # == elif num != 10:
    print('not equal to 10')
elif num not in [10, 20]:
    print('not equal to 10 or 20')
else:
    print('greater than 20')

# which value will be consider as False
if not "":
    print('empty string')

if not ():
    print('empty tuple')

if not []:
    print('empty list')

if not None:
    print('none')

#  ofen use in script name == '__main__'
if __name__ == '__main':
    print('excute as a single script')