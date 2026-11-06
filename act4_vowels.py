sentence = input("Enter a sentence: ")

vowels = "aeiouAEIOU"
count = 0

for letter in sentence:
    if letter in vowels:
        count += 1

print("Vowels:", count)
