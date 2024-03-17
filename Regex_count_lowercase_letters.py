"""https://www.codewars.com/kata/56a946cd7bd95ccab2000055/train/python
Your task is simply to count the total number of lowercase letters in a string.

Examples
"abc" ===> 3

"abcABC123" ===> 3

"abcABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~" ===> 3

"" ===> 0;

"ABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~" ===> 0

"abcdefghijklmnopqrstuvwxyz" ===> 26
"""
def lowercase_count(strng):
    count = 0
    if strng == "": return 0
    for i in strng:
        if i.islower():
            count+=1
            
    return count
   # variant 2 return sum(1 for i in strng if i.islower())

print(lowercase_count("abc"))
print(lowercase_count("abcABC123"))
print(lowercase_count("abcABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~"))
print(lowercase_count(" "))
print(lowercase_count(""))
print(lowercase_count("abcdefghijklmnopqrstuvwxyz"))