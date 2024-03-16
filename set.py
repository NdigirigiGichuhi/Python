#!/usr/bin/python3

set1 = set()
set2 = set()

i = 0

while(i < 5):
    set1.add(int(input("Enter set1 data: ")))
    i += 1

i = 0

while(i < 5):
    set2.add(int(input("Enter set2 data: ")))
    i += 1

set3 = set1 & set2
print(set3)
