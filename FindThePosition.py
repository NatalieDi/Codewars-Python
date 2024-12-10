#  https://www.codewars.com/kata/5808e2006b65bff35500008f/train/python


import string


def position(alphabet):
    asc = string.ascii_lowercase
    return f"Position of alphabet: {asc.find(alphabet)+1}"


print(position("a"))  # 1
print(position("z"))  # 26
print(position("e"))  # 5
