# https://dodona.ugent.be/nl/courses/1286/series/14346/activities/723647984

import math

getal1= int(input("Geef een getal: "))
getal2= int(input("Geef een getal: "))
getal3= int(input("Geef een getal: "))

minimum = min(getal1, getal2, getal3)
maximum = max(getal1, getal2, getal3)
average = (getal1 + getal2 + getal3) / 3
average = round(average, 2)

print(f"maximum: {maximum}")
print(f"minimum: {minimum}")
print("average: {:.2f}".format(average)) #Zorgt voor dat het maar op 0.0 eindigt en niet 0.00