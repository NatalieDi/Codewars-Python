"""https://www.codewars.com/kata/53da3dbb4a5168369a0000fe/train/python
"""


def evenodd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(evenodd(-1))
print(evenodd(0))
print(evenodd(1))
print(evenodd(4))
