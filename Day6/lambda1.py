import time

add=lambda x,y: x+y
print(add(5, 3))  # Output: 8

find_longest_word = lambda s: max(s.split(), key=len)
sentence = input("Enter a string: ")

#start time
start_time=time.perf_counter()

result = find_longest_word(sentence)

#end time
end_time=time.perf_counter()

print("The longest word in the string is:", result)

#execution time
execution_time=end_time-start_time
print(f"Execution time: {execution_time:.6f} seconds")