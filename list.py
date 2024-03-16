#!/usr/bin/python3

numbers = []
total = 0
i = 0
while (i < 5 ):
    num = input("Enter number: ")
    num = int(num)
    numbers.append(num)
    i += 1

for number in numbers:
    total += number

print(total)
