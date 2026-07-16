def count_vowels(s):
    vowel_count = {
        'a': 0,
        'e': 0, 
        'i': 0,
        'o': 0,
        'u': 0
    }

    for ch in s.lower():
        if ch in vowel_count:
            vowel_count[ch] += 1

    return vowel_count

sentence = input("Enter a string: ")
res = count_vowels(sentence)
print("The number of each vowel in the string is:")
for vowel, count in res.items():
    print(f"{vowel}: {count}")
    