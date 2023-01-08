# https://dodona.ugent.be/nl/courses/1286/series/14345/activities/819600301


# Lees het aantal stapels en het aantal goudstukken in elke stapel in
n = int(input())

# Lees het gewicht van een echt goudstuk in
gewicht_echt = int(input())

# Lees het gewicht van alle goudstukken samen in
gewicht_totaal = int(input())

# Bepaal het aantal goudstukken van de vervalste stapel
vervalst = (gewicht_totaal - n * gewicht_echt) / (gewicht_echt - 1)

# Print het aantal goudstukken van de vervalste stapel
print(int(vervalst))
