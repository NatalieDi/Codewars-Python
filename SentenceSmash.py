#  https://www.codewars.com/kata/53dc23c68a0c93699800041d/train/python


def smash(words):
    if len(words) == 0:
        return ""
    if len(words) == 1:
        return words[0]
    else:
        return ' '.join(words)


print(smash(["hello", "world"]))  # "hello world"
print(smash(["hello", "amazing", "world"]))  # "hello amazing world"
print(smash(["this", "is", "a", "really", "long", "sentence"]))  # "this is a really long sentence"
