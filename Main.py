from Employee import Employee
from Person import Person

harris = Employee(14, 'harris', 25)
print(issubclass(Employee, Person))

print(isinstance(harris, Person))
print(isinstance(harris, Employee))

print(harris.__repr__())
print(harris.__str__())

han = Employee(14, 'harris', 25)
print(harris == han)
print(Employee._Employee__counter)
