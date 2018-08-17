class Towar():

    material = "plastik"

    def nazwa(self):
        return ("towar")

xxx = Towar()

print(xxx.nazwa())


class Towary():

    rozmiar = 'duzy'
    koszt = 500

    def __init__(self, cena, material='nieznany', kolor='nieznany'):
        self.cena = cena
        self.material = material
        self.kolor = kolor

    @classmethod
    def price_in_euro(cls):
        return cls.koszt * 4

    def price2(self):
        return self.cena * 5


class Towar2(Towary):

    def __str__(self):
        return "opis"

    rozmiar = 'maly'


nowy = Towary(5000)

nowy2 = Towary(300, "Plastik", 'zielony')
nowy3 = Towar2(500)
print(nowy.kolor)
print(nowy2.kolor)
print(Towary.price_in_euro())
print(nowy2.price2())
print(nowy3.rozmiar)