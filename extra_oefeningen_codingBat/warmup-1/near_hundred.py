"""
Given an int n, return True if it is within 10 of 100 or 200.
Note: abs(num) computes the absolute value of a number.

near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False
"""

def near_hundred(n):
    verschil_100 = 100 - n
    som_100 = 100 + n
    verschil_200 = 200 - n
    som_200 = 200 + n
    if abs(verschil_100) < 11 or abs(verschil_200) < 11 or ( som_100 > 109 and som_100 < 111 ) or (som_200 > 209 and som_200 < 211):
        return True
    else:
        return False

print(near_hundred(111))
