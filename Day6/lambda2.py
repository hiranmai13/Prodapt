#accept list
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

#filter even numbers
even=list(filter(lambda x: x % 2 == 0, numbers))

squared_even=list(map(lambda x: x**2, even))

print("The squared even numbers are:", squared_even) 