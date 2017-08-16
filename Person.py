class Person:
 """A general person class"""
 def __init__(self, name, age):
     self.name = name
     self.age = age

 def __del__(self):
     print(self.name + ' is reclaimed.')

 def wakeup(self, at):
      print('{0} wake up at {1} am'.format(self.name, at))