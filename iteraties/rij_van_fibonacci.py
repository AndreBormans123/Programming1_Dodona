# https://dodona.ugent.be/nl/courses/1286/series/14348/activities/1952876754


getal = int(input("Geef een getal in: "))

a, b = 0, 1
while a < getal:
    print(a)
    a, b = b, a+b
