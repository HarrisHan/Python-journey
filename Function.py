def a_stub_function():
    pass

# all the function in python has a return value defult is None
def add(m, n):
    return m + n

add(1, 2)
add(n=2, m = 1)

def add(m=2, n=1):
    return m + n
add()

def add(*args):
    tmp = 0

    for i in args:
        tmp += i

    return  tmp

# *args refers to many params * means many args is just a alternative symbols
print(add(1, 2, 3, 4, 5))

def add(**args):  # ** means so many keyword params
    tmp = 0

    for i in  args:
        tmp += args[i]

    return tmp

print(add(n1=1, n2=2, n3=3, n4=4, n5=5))

def add(*args, **k_args):
    tmp = 0

    for i in args:
        tmp += i

    for i in k_args:
        tmp += k_args[i]

    return  tmp

print(add(4, 5, n1=1, n2=2, n3=3))