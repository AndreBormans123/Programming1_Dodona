# https://dodona.ugent.be/nl/courses/1286/series/14348/activities/1317066143
def bier_op_muur(aantal, enkelvoud, meervoud):
  for i in range(1, aantal):
    print(meervoud.format(aantal))
    aantal -= 1
    if aantal == 1:
      print(enkelvoud.format(aantal))
      print(meervoud.format(aantal))
      print(enkelvoud.format(0))
      break
    print(enkelvoud.format(aantal))

getal = int(input("Geef een getal in: "))

bier_op_muur(getal, "{} flesje met bier op de muur, {} flesje met bier.", "{} flesjes met bier op de muur, {} flesjes met bier.")