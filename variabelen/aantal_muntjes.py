# https://dodona.ugent.be/nl/courses/1286/series/14345/activities/715315832

# bedrag (in cent)


bedrag = 1156

dollar = int(bedrag / 100)
bedrag = bedrag - dollar *100
kwartje = int(bedrag/25)
bedrag = bedrag - kwartje *25
dubbeltje = int(bedrag/10)
bedrag = bedrag - dubbeltje *10
stuiver = int(bedrag/5)
bedrag = bedrag - stuiver *5
cent = int(bedrag)


print(f"Dollars: {int(dollar)}")
print(f"Kwartjes: {int(kwartje)}")
print(f"Dubbeltjes: {int(dubbeltje)}")
print(f"Stuivers: {int(stuiver)}")
print(f"Centen: {int(cent)}")