# https://dodona.ugent.be/nl/courses/1286/series/14353/activities/1624746422


aantal_cijfers = int(input("Hoeveel cijfers wil je ingeven? "))
even = []
oneven = []

for i in range(1, aantal_cijfers + 1):
    getallen = int(input(f"Geef cijfer {i} in: "))
    if getallen % 2 == 0:
        even.append(getallen)
    elif not getallen % 2 == 0:
        oneven.append(getallen)

print(even)
print(oneven)