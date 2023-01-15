zin = input("Geef een zin in: ")

lower_zin = zin.lower()
sets = set()
counter_10  = 0
counter_3 = 0
counter_woorden = 0

for i in lower_zin.split(" "):
    if i.isalpha():
        sets.add(i)
        if len(i) > 10:
            counter_10 += 1
        if len(i) % 3 == 0:
            counter_3 += 1

word_lengths = sum(len(word) for word in sets)
average_length = word_lengths / len(sets)

print(sets)
print(f"Er zijn {counter_10} woorden die langer zijn dan 10")
print(f"Er zijn {counter_3} woorden waarvan de lengte een veelvoud is van 3")
print(f"De gemiddelde lengte van alle unieke woorden is: {average_length:.2f} tekens")