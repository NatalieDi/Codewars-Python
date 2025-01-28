# www.codewars.com/kata/57ab3c09bb994429df000a4a/train/python


def two_highest(arg1):
    unique_values = list(set(arg1))
    unique_values.sort(reverse=True)
    return unique_values[:2]


print(two_highest([1, 1, 1]))  # [1]
print(two_highest([15, 20, 20, 17]))  # [20, 17]
print(two_highest([]))  # []
