#  https://www.codewars.com/kata/5875b200d520904a04000003/train/python


def enough(cap, on, wait):
    return on+wait-cap if on+wait > cap else 0


print(enough(10, 5, 5))  # 0
print(enough(100, 60, 50))  # 10
print(enough(20, 5, 5))  # 0
