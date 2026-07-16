from typing import TypedDict

class Student(TypedDict):
    id: int
    name: str
    age: int

student1=Student(id=1, name="Alice",age=20)
student2=Student(id='101',name="Bob",age=22) # type: ignore
print(student1)
print(student2)

#TypeDict will convertthe result into dict format
#mpy catches the error before you run program
#pip install mypy
#run as mypy student.py