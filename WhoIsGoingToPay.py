#  https://www.codewars.com/kata/58bf9bd943fadb2a980000a7/train/python


def who_is_paying(name):
    if len(name)>2: return [name, name[0:2]]
    else:
        return [name]


print(who_is_paying("Mexico"))  # ["Mexico", "Me"]
print(who_is_paying("Melania"))  # ["Melania", "Me"]
print(who_is_paying("Melissa"))  # ["Melissa", "Me"]
print(who_is_paying("Me"))  # ["Me"]
print(who_is_paying(""))  # [""]
print(who_is_paying("I"))  # ["I"]
