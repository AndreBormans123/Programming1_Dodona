class Verkeerslicht:
    def __init__(self, toestand="rood"):
        self.toestand= toestand
        if not (toestand == "rood" or toestand == "groen" or toestand == "oranje"): #Ook met asser mogelijk
            raise AssertionError("Verkeerde waarde ingegeven")
    
    def __str__(self) -> str:
        return f"{self.toestand}"
    
    def __repr__(self) -> str:
        return f"Verkeerslicht('{self.toestand}')"

    def volgende(self):
        if self.toestand == 'rood': 
            self.toestand == 'groen'
        elif self.toestand == 'groen':
            self.toestand == 'oranje'
        elif self.toestand == 'oranje':
            self.toestand == 'rood'

licht1= Verkeerslicht()
licht2 = Verkeerslicht('groen')
print(licht1, licht2)