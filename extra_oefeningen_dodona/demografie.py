class Stad:
    def __init__(self, naam, inwoners=5000):
        self.naam = naam
        self.inwoners = inwoners

        if self.inwoners < 70:
            raise ValueError("Het aantal inwoners moet minstens 70 zijn.")
    
    def heeft_meer_inwoners(self, andere_stad):
        return self.inwoners > andere_stad.inwoners
    
    def __eq__(self, andere_stad):
        return self.naam == andere_stad.naam
    
    def __str__(self):
        return f"{self.naam} heeft {self.inwoners} inwoners"

class Demografie:
    def __init__(self, regio_naam):
        self.regio_naam = regio_naam
        self.steden = []
    
    def voeg_stad_toe(self, stad):
        if stad in self.steden:
            raise ValueError("Stad bestaat al in lijst.")
        
        self.steden.append(stad)
        self.steden = sorted(self.steden, key=lambda stad: stad.inwoners)
    
    def bereken_totaal_aantal_inwoners(self):
        totaal_inwoners = 0
        for stad in self.steden:
            totaal_inwoners += stad.inwoners
        return totaal_inwoners
    
    def fusioneer(self, stad1_naam, stad2_naam, nieuwe_stad_naam):
        stad1 = None
        stad2 = None
        for stad in self.steden:
            if stad.naam == stad1_naam:
                stad1 = stad
            elif stad.naam == stad2_naam:
                stad2 = stad
        
        if stad1 is None:
            raise ValueError("Stad 1 bestaat niet in lijst.")
        if stad2 is None:
            raise ValueError("Stad 2 bestaat niet in lijst.")
        
        nieuwe_stad = Stad(nieuwe_stad_naam, stad1.inwoners + stad2.inwoners)
        self.steden.remove(stad1)
        self.steden.remove(stad2)
        self.steden.append(nieuwe_stad)
        self.steden = sorted(self.steden, key=lambda stad: stad.inwoners)
    
    def geef_steden_met_minimum_aantal_inwoners(self, minimum_inwoners):
        return [stad for stad in self.steden if stad.inwoners >= minimum_inwoners]
    
    def __str__(self): #steden
        steden_string = "\n".join([str(stad) for stad in self.steden])