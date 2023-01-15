"""
Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'
"""

def string_bits(str):
    new_string = ""
    for i in range(0, len(str)):
        new_string += str[:i + 1]
    return new_string

print(string_bits("Hello"))
