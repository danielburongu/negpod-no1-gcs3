#!/usr/bin/python3
letters = input("Type any word: ").lower()
vowles = ["a", "e", "i", "o", "u", "y"]

i = 0
while i < len(letters):
    if letters[i] in vowels:
        letters = letters.replace(letters[i], "")
        continue
    i += 1
print("\nWithout Vowels =", letters)
