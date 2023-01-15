from demografie import Stad, Demografie

# Maak steden
leuven = Stad("Leuven", 102000)
duh = Stad("Duh", 5000)
gent = Stad("Gent", 263429)
hasselt = Stad("Hasselt", 80000)
genk = Stad("Genk", 85000)

# Maak demografie en voeg steden toe
demografie = Demografie("Vlaanderen")
demografie.voeg_stad_toe(duh)
demografie.voeg_stad_toe(hasselt)
demografie.voeg_stad_toe(genk)
demografie.voeg_stad_toe(leuven)
demografie.voeg_stad_toe(gent)

# Print demografie
#print(demografie)

# Fusioneer steden
demografie.fusioneer("Gent", "Duh", "GentPlus")

# Print demografie
#print(demografie)

# Geef steden met minimaal 100000 inwoners
print("\nsteden met meer dan 100000 inwoners:")
for stad in demografie.geef_steden_met_minimum_aantal_inwoners(100000):
    print(stad)