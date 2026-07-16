from shapes import circle, rectangle
from ecommerce import cart, payment
from utilities import string_ops, math_ops
from school import students, results
from banking import transactions, accounts

print("======SHAPES======")
print(circle.area(5))
print(rectangle.area(10,4))

print("\n=====ECOMMERCE=======")
cart.add_item("Laptop")
cart.add_item("Mouse")
total=cart.calculate_total([50000, 1000])
print("Total: ",total)
payment.process_payment(total)

print("\n=====UTILITIES======")
print(string_ops.count_vowels("Python Programming"))
print(math_ops.mean([10,20,30,40]))

print("\n=======SCHOOL======")
students.add_student("Asha")
print(students.view_students())
print(results.calculate_grade(88))

print("\n=====BANKING=====")
transactions.deposit(500)
print(accounts.get_balance())