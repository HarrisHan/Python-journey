try:
    3/0
except ZeroDivisionError:
    print('Divide by zero')

try:
    fn()
except ZeroDivisionError:
    print('Divide by 0')
except NameError:
    print('Invalid name')

try:
    "Hello".index(1)
except ZeroDivisionError:
    print('Divide by 0')
except NameError:
    print('Invalid name')
except:
    print('default handler')

try:
    fn()
except ZeroDivisionError:
    print('Divide by 0')
except NameError:
    print('Invalid name')
finally:
    print('Clean up actions')

try:
    3/1
except ZeroDivisionError:
    print('Divide by zero')
else:
    print('no errors')
finally:
    print('clean up actions')
