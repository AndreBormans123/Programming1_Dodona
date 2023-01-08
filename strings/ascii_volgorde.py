# https://dodona.ugent.be/nl/courses/1286/series/14351/activities/335876740


def sort_string_ascii(string):
  sorted_string = ''
  while len(string) > 0:
    min_char = min(string)
    sorted_string += min_char
    string = string.replace(min_char, '', 1)
  return sorted_string

string = input("Geef een zin in: ")
sorted_string = sort_string_ascii(string)
print(sorted_string)
