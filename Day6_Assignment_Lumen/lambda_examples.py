from functools import reduce

employees = [("Asha", 85),("Bala",92),("Chitra",78)]
print(sorted(employees, key=lambda x: x[1], reverse=True))

readings=[2,3,4]
print(list(map(lambda x: x**2, readings)))

player_ids=[101,102,103,104,105]
print(list(filter(lambda x: x%2!=0, player_ids)))

dimensions=[2,3,5]
print(reduce(lambda x,y: x*y, dimensions))

students_marks={
    "Asha":78,
    "Bala":90,
    "Chitra":65
}

print(sorted(
    students_marks.items(),
    key=lambda x: x[1],
    reverse=True
))