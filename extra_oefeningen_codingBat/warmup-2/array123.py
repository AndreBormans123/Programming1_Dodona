"""
Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True
"""

def array123(nums):
    mystr = " ".join(map(str, nums))
    print(mystr)
    common = ""
    for i in range(0, len(mystr)):
        common = mystr[:i + 1]
        if "1 2 3" in common:
            return True
    return False

print(array123([1, 1, 2, 3, 1]))