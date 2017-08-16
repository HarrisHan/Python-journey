class Person:
 """A general person class"""
 def __init__(self, name, age):
     self.name = name
     self.age = age

 def __del__(self):
     print(self.name + ' is reclaimed.')

 def wakeup(self, at):
      print('{0} wake up at {1} am'.format(self.name, at))


harris = Person('Harris', 25)
han = harris

print(id(harris))
print(id(han))

del han
print('only 1 ref')

del harris
# print(harris.name)
# print(harris.age)

# harris.wakeup(8)
# harris.wakeup(at=8)

# access class property
# print(hasattr(harris, 'name'))
#
# # getter & setter
# print(getattr(harris,'name'))
# setattr(harris, 'name', 'ruby')
# print(getattr(harris,'name'))
#
# delattr(harris, 'name')
# print(getattr(harris, 'name')) # AttributeError

