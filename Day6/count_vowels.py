def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0

    for ch in s.lower():
        if ch in vowels:
            count += 1
    return count

sentence=input("Enter a string: ")

res=count_vowels(sentence)
print("The Number of vowels = ",res)
# print(f"The number of vowels in '{sentence}' is: {res}")