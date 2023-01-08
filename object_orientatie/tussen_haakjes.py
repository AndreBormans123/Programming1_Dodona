# https://dodona.ugent.be/nl/courses/1286/series/14351/activities/954463058

def getHaakjes(zin):
    haakje = False
    char = ""
    for letter in zin:
        if letter == "[":
            haakje = True
        elif letter == "]":
            haakje = False
        elif haakje == True:
            char += letter

    return char
zin = input("Geef een zin in: ")

print(getHaakjes(zin))