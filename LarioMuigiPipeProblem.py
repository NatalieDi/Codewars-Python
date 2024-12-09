#  https://www.codewars.com/kata/56b29582461215098d00000f/train/python


def pipe_fix(nums):
    return [number for number in range(nums[0], nums[-1]+1)]


print(pipe_fix([1, 2, 3, 5, 6, 8, 9]))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(pipe_fix([1, 2, 3, 12]))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(pipe_fix([6, 9]))  # [6, 7, 8, 9]
print(pipe_fix([-1, 4]))  # [-1, 0, 1, 2, 3, 4]
print(pipe_fix([1, 2, 3]))  # [[1, 2, 3]
