# https://dodona.ugent.be/nl/courses/1286/series/14348/activities/1169713984


getal = int(input("Geef een getal in: "))
aantal = 1

while aantal < 11:
    berekening = aantal * getal
    print(f"{aantal} * {getal} = {berekening}")
    aantal += 1
    