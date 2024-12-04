"""
https://www.codewars.com/kata/5f70c883e10f9e0001c89673/train/python
"""


def flip(d, a):
    if d == 'R':
        return sorted(a)
    if d == 'L':
        return sorted(a, reverse=True)


print(flip('R', [3, 2, 1, 2]))
