#  https://www.codewars.com/kata/5601409514fc93442500010b/train/python


def better_than_average(class_points, your_points):
    arg = sum(class_points) / len(class_points)
    return True if arg <= your_points else False


print(better_than_average([2, 3], 5))  # true
print(better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75))  # true
print(better_than_average([12, 23, 34, 45, 56, 67, 78, 89, 90], 69))  # true
print(better_than_average([29, 55, 74, 60, 11, 90, 67, 28], 21))  # false

