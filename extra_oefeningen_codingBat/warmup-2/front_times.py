"""
Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;

front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc'
"""


def front3(str, n):
    if len(str) < 3:
        letters = str * n
        return letters
    else:
        letters = str[0:3]
        letters = letters * n
        return letters
