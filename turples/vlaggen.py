# https://dodona.ugent.be/nl/courses/1286/series/14352/activities/1294363212

def vlag(richting, kleuren):
    kleur = ""
    if richting == "verticaal":
        for i in range(0, len(kleuren)):
            if i == len(kleuren) -1:
                kleur += kleuren[i]
            else:
                kleur += kleuren[i] + " | " 

        
    elif richting == "horizontaal":
        for x in range(0, len(kleuren)):
            if x == len(kleuren) -1:
                kleur += kleuren[x]  
            else:
                kleur += kleuren[x] + "\n" + "-" + "\n"
    return kleur

welke_richting = "horizontaal"
turple_kleuren = ("zwart", "geel", "rood")
print(vlag(welke_richting, turple_kleuren))