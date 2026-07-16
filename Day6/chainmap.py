from collections import ChainMap

student={
    "Name":"John",
    "Age":20,   
}

course={
    "Course":"Python",
    "Duration":"3 months"
}

combined=ChainMap(student,course)
print(combined)  # Output: ChainMap({'Name': 'John', 'Age': 20}, {'Course': 'Python', 'Duration': '3 months'})