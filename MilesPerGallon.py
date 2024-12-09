#https://www.codewars.com/kata/557b5e0bddf29d861400005d/train/python


def converter(mpg):
    return round((mpg * 1.609344 / 4.54609188), 2)


print(converter(10))  # 3.54
print(converter(20))  # 7.08
print(converter(30))  # 10.62
print(converter(24))  # 8.5
print(converter(36))  # 12.74

