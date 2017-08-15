doubleQuoters = "hello"
single = 'hello'

triple = '''hello
This is a long string 
through multiple lines.
'''

doubleQuoters = "hello 'python'"
single = 'hello python'

triple = '''hello 'python'
this is a long string
acrossing multiple lines.
'''

aNumber = 123
aString = str(aNumber)
# 字符串只读

doubleQuoters = u"hello python!"
action = "Hello"
name = "Mars!"
welcome = action + name

welcome.upper()
welcome.lower()

action.strip()

print(dir(action))

# print(help(action.count)

action[0]

# c
# printf("Hello %s!","Mars")

name = "Mars"
print("%s %s" % ("Hello", name))

welcome = {"action": "Hello", "name": "Mars"}
print("%(action)s %(name)s" % welcome)

print("{0} {1}!".format("Hello", "Mars"))


print("{action} {name}!".format(**welcome))  ## Welcome Mars!
