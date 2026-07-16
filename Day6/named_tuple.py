from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'grade'])
s1=Student('Alice',20,'A')
print(s1.name)  # Output: Alice
print(s1.age)   # Output: 20
print(s1.grade) # Output: A