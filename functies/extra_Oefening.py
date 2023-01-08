num11, num12, num13 = 436, 178, 992
num21, num22, num23 = 880, 543, 101

def kleinste_van_twee( n1, n2 ):
    if n1 < n2:
        return n1
    return n2

def grootste_van_twee( n1, n2 ):
    if n1 > n2:
        return n1
    return n2

def verwijder_een_van_drie( n1, n2, n3, verwijder ):
    if n1 == verwijder:
        return n2, n3
    elif n2 == verwijder:
        return n1, n3
    return n1, n2

def verwijder_een_van_twee( n1, n2, verwijder ):
    if n1 == verwijder:
        return n2
    return n1

def verwijder_twee_van_drie( n1, n2, n3, verwijder1, verwijder2):
    num1, num2 = verwijder_een_van_drie( n1, n2, n3, verwijder1 )
    return verwijder_een_van_twee( num1, num2, verwijder2 )

def kleinste( n1, n2, n3 ):
    return kleinste_van_twee( kleinste_van_twee( n1, n2 ), n3 )

def middelste( n1, n2, n3 ):
    return verwijder_twee_van_drie( n1, n2, n3, 
        kleinste( n1, n2, n3 ), grootste( n1, n2, n3 ) )

def grootste( n1, n2, n3 ):
    return grootste_van_twee( grootste_van_twee( n1, n2 ), n3 )

print( "som van kleinste =", kleinste( num11, num12, num13 ) + 
    kleinste( num21, num22, num23 ) )
print( "som van middelste =", middelste( num11, num12, num13 ) + 
    middelste( num21, num22, num23 ) )
print( "som van grootste =", grootste( num11, num12, num13 ) + 
    grootste( num21, num22, num23 ) )