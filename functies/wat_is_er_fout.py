# https://dodona.ugent.be/nl/courses/1286/series/14349/activities/750340336

# Deze manier
""" def oppervlakte_van_driehoek( basis, hoogte ):
    opp = 0.5 * basis * hoogte
    return basis, hoogte, opp

basis, hoogte, opp = oppervlakte_van_driehoek(4.5, 1)

print( "Een driehoek met basis", basis, "en hoogte", hoogte, "heeft oppervlakte", opp )

 """

#OF

#Deze manier
def oppervlakte_van_driehoek( basis, hoogte ):
    opp = 0.5 * basis * hoogte
    output = "Een driehoek met basis " + str(basis) + " en hoogte " + str(hoogte) + " heeft oppervlakte " + str(opp)
    return output