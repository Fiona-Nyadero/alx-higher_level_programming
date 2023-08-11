#!/usr/bin/python3
def to_gros(character):
    if ord(character) >= 97 and ord(character) <= 122:
        return (ord(character) - 32)
    else:
        return ord(character)


def uppercase(str):
    neu = ""
    for character in str:
        neu += "%c" % to_gros(character)
    print("{:s}".format(neu))
