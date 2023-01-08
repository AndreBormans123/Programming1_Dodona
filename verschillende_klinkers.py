# https://dodona.ugent.be/nl/courses/1286/series/14347/activities/1014821966


text = input("Geef een tekst in: ")


klinkers = "aeiouAEIOU"
counter = 0

if text in klinkers:
    counter += 1
elif text == "e":
    counter += 1
elif text == "i":
    counter += 1
elif text == "o":
    counter += 1
elif text == "u":
    counter += 1
elif text == "A":
    counter += 1
elif text == "E":
    counter += 1
elif text == "I":
    counter += 1
elif text == "O":
    counter += 1
elif text == "U":
    counter += 1
else:
    print("De zin bevat geen klinkers.")
print("De zin bevat", counter, "klinkers.")


