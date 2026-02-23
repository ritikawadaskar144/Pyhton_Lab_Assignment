# Lab Assignment 1

text = input("Enter a string: ")
vowels = 0
consonants = 0
spaces = 0
lowercase = 0
for ch in text:
    if ch in "aeiouAEIOU":
        vowels += 1
    elif ch.isalpha():  # checks if character is a letter
        consonants += 1

    if ch == " ":
        spaces += 1

    if ch.islower():
        lowercase += 1

print("Number of Vowels:", vowels)
print("Number of Consonants:", consonants)
print("Number of Spaces:", spaces)
print("Number of Lowercase Letters:", lowercase)


# Lab Assignment 2

sentence = input("Enter a sentence: ")

result = sentence.upper()

print("Output:", result)