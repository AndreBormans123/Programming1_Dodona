# https://dodona.ugent.be/nl/courses/1286/series/14348/activities/1159766268

""" zin1 = input("Geef een zin in: ")
zin2 = input("Geef een tweede zin in: ")
gemeenschappelijk = ""

for i in zin2:
    for x in zin1:
        if x == i:
            gemeenschappelijk += x
            break
print(gemeenschappelijk)



             """

def common_characters(string1, string2):
  common_chars = []
  for char in string1:
    if char in string2 and char not in common_chars:
      common_chars.append(char)
  return "".join(common_chars)

string1 = input("Geef zin 1 in: ")
string2 = input("Geef zin 2 twee in: ")
print(common_characters(string1, string2))