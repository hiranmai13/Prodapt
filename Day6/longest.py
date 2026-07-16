def longest_word(s):
    x=[]
    x= s.split()
    print(x)
    longest = max(x, key=len)

    # for word in x:
    #     if len(word) > len(longest):
    #         longest = word
            
    # return longest

#different approach
def find_longest_word(s):
    return max(s.split(), key=len)

sentence = input("Enter a string: ")
result = longest_word(sentence)
print("The longest word in the string is:", result)

