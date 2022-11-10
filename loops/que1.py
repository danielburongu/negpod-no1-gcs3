#!/usr/bin/python3
#Python program that takes an integer and prints all odd numbers up to the said integer
number = int(input('Enter an integer: '  ))
for num in range(number):
    if num % 2 != 0:
        print(num, end = ' ')
