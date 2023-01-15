class ISBN13:
    def __init__(self, getal, lengte=1):
        self.getal = str(getal)
        self.lengte = lengte
        if not (int(lengte) > 0 and int(lengte) < 6):
            raise AssertionError("AssertionError: ongeldige ISBN code")
    
    def __str__(self):
        return f"{self.getal[:3]}-{self.getal[3]}-{self.getal[4:12]}-{self.getal[-1]}"
    
    def __repr__(self):
        return f"ISBN13({self.getal}, {self.lengte})"

    def isgeldig(self):
        return True
    
    def alsISBN10(self):
        isbn10 = self.getal[:3]
        if not "978" in isbn10:
            return None
        else:
            return f"{self.getal[3]}-{self.getal[4:12]}-3"

code_01 = ISBN13(6-48462023-3)
print(code_01.alsISBN10())

