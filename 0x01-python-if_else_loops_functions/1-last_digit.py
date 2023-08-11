#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_dgt = abs(number) % 10

if number < 0:
    l_dgt *= -1

print("Last digit of {0:d} is {1:d}".format(number, l_dgt), end=" ")

if l_dgt > 5:
    print("and is greater than 5")
elif l_dgt == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
