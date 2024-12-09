#  https://www.codewars.com/kata/57280481e8118511f7000ffa/train/python


def split_and_merge(string_, separator):
    words = string_.split(' ')
    array = []
    for i in words:
        i = separator.join(i)
        array.append(i)
    return ' '.join(array)


print(split_and_merge("My name is John", " "))  # "M y n a m e i s J o h n"
print(split_and_merge("My name is John", "-"))  # "M-y n-a-m-e i-s J-o-h-n"
print(split_and_merge("Hello World!", "."))  # "H.e.l.l.o W.o.r.l.d.!"
print(split_and_merge("Hello World!", ","))  # "H,e,l,l,o W,o,r,l,d,!"
