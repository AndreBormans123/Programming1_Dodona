# https://dodona.ugent.be/nl/courses/1286/series/14348/activities/191240337


def sum_of_squares(a, b):
  results = []
  for i in range(a, b+1):
    for j in range(i, b+1):
      if i**2 + j**2 == a:
        results.append(f"{a} = {i}^2 + {j}^2")
  return results

a = 1
b = 50
print(sum_of_squares(a, b))
