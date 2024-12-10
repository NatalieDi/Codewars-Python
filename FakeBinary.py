#   https://www.codewars.com/kata/57eae65a4321032ce000002d/train/python


def fake_bin(x):
    str = ''
    for i in x:
        if int(i) < 5:
            str+='0'
        else: str+='1'
    return str


print(fake_bin("45385593107843568"))  # "01011110001100111"
print(fake_bin("509321967506747"))  # "101000111101101"
print(fake_bin("366058562030849490134388085"))  # "011011110000101010000011011"
print(fake_bin("800857237867"))  # "100111001111"
