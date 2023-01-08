# https://dodona.ugent.be/nl/courses/1286/series/14361/activities/2096226599


class BankRekening:
    def __init__(self, name, rekeningsnummer, bedrag=0):
      self.name = name
      self.rekeningsnummer = rekeningsnummer
      self.bedrag = bedrag

    def __str__(self):
        return f"{self.name}, {self.rekeningsnummer}, bedrag: {self.bedrag}"

    def __repr__(self):
           return "BankRekening('{}', '{}', {})".format(self.name, self.rekeningsnummer, self.bedrag)

    def storten(self, geld):
        self.bedrag += geld

    def afhalen(self, geld):
        self.bedrag -= geld

