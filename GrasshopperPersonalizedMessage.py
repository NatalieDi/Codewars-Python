"""https://www.codewars.com/kata/5772da22b89313a4d50012f7/python
Description
Create a function that gives a personalized greeting. This function takes two parameters: name and owner.

Use conditionals to return the proper message:

case	return
name equals owner	'Hello boss'
otherwise	'Hello guest'
FUNDAMENTALS STRINGS """


def greet(name, owner):
    if name == owner:
        return 'Hello boss'
    else:
        return 'Hello guest'


print(greet('Greg', 'Daniel'))
print(greet('Daniel', 'Daniel'))
