# https://dodona.ugent.be/nl/courses/1286/series/14348/activities/1317066143


getal = int(input("Geef een getal in: "))

for i in range(1, getal):
    print(f"{getal} flesjes met bier op de muur, {getal} flesjes met bier.")
    getal -= 1
    if getal == 1:
        print("Open er een, drink hem meteen, 1 flesje met bier op de muur.")
        print("1 flesje met bier op de muur, 1 flesje met bier.")
        print("Open er een, drink hem meteen, 0 flesjes met bier op de muur.")
        break
    print(f"Open er een, drink hem meteen, {getal} flesjes met bier op de muur.")