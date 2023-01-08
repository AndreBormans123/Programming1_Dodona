# https://dodona.ugent.be/nl/courses/1286/series/14346/activities/723647984


from decimal import MAX_EMAX


getal1 = int(input("Getal 1: "))
getal2 = int(input("Getal 2: "))
getal3 = int(input("Getal 3: "))

max = max(getal1, getal2, getal3)
min = min(getal1, getal2, getal3)
avg = (getal1 + getal2 + getal3) /3
avg = round(avg,2)

print("maximum: {}".format(max))
print("minimum: {}".format(min))
print("gemiddelde: {}".format(avg))

