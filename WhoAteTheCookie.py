#  https://www.codewars.com/kata/55a996e0e8520afab9000055/train/python


def cookie(x):
    if type(x) is str:
        return "Who ate the last cookie? It was Zach!"
    if type(x) is int or type(x) is float:
        return "Who ate the last cookie? It was Monica!"
    return "Who ate the last cookie? It was the dog!"


print(cookie("Ryan"))  # "Who ate the last cookie? It was Zach!"
print(cookie(2.3))  # "Who ate the last cookie? It was Monica!"
print(cookie(26))  # "Who ate the last cookie? It was Monica!"
print(cookie(True))  # "Who ate the last cookie? It was the dog!"
