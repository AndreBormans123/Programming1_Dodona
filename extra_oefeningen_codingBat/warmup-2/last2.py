"""
Given a string, 
return the count of the number of times that a substring length 2 appears in the string
and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2

The function "last2" takes in a string as input and returns the count of the number of times that a substring 
of length 2 appears in the string, except for when it appears as the last 2 characters of the string. 
The input string 'hixxxhi' will return 1 because the substring 'hi' appears once in the string, 
but not as the last 2 characters of the string. 'xaxxaxaxx' will also return 1 for the same reason, 
and 'axxxaaxx' will return 2 because the substring 'ax' appears twice in the string, 
but not as the last 2 characters.
"""

def last2(str):
  # Screen out too-short string case.
  if len(str) < 2:
    return 0
  
  # last 2 chars, can be written as str[-2:]
  last2 = str[len(str)-2:]
  count = 0
  
  # Check each substring length 2 starting at i
  for i in range(len(str)-2):
    sub = str[i:i+2]
    if sub == last2:
      count = count + 1

  return count

print(last2("hixxhi"))