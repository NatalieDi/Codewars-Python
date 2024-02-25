"""https://www.codewars.com/kata/5966e33c4e686b508700002d/train/python
Description
Create a function that takes 2 integers in form of a string as an input, and outputs the sum (also as a string):

Example: (Input1, Input2 -->Output)

"4",  "5" --> "9"
"34", "5" --> "39"
"", "" --> "0"
"2", "" --> "2"
"-5", "3" --> "-2"
Notes:

If either input is an empty string, consider it as zero.

Inputs and the expected output will never exceed the signed 32-bit integer limit (2^31 - 1)

FUNDAMENTALS"""


def sum_str(a, b):
    if (a == "" and b == ""):
        return "0"
    if (a == ""):
        return b;
    if (b == ""):
        return a;
    return str(int(a) + int(b))


print(sum_str("4", "5"))  # 9
print(sum_str("34", "5"))  # 39
print(sum_str("", ""))  # 0
print(sum_str("2", ""))  # 2
print(sum_str("-5", "3"))  # -2
