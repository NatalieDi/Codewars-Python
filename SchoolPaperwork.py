#  https://www.codewars.com/kata/55f9b48403f6b87a7c0000bd/train/python


def paperwork(n, m):
    if n < 0 or m < 0:
        return 0
    else:
        return n*m


print(paperwork(5, 5))  # 25
print(paperwork(1, 2))  # 2
print(paperwork(-5, 5))  # 0
print(paperwork(5, -5))  # 0
print(paperwork(-5, -5))  # 0
print(paperwork(5, 0))  # 0
