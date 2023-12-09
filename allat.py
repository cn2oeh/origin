class Allat:
    def __init__(self, nev):
        self._nev = nev

    def nevetmond(self):
        print(f"A nevem {self._nev}.")

class Negylabu:
    LABAK_SZAMA = 4
    def __init__(self):
        print(f"Négylábú vagyok. {self.LABAK_SZAMA}")
class Kutya(Allat):
    faj = "puli"

    def ugat(self):
        print("Vuff!")

    def nevetmond(self):
        print(f"Én egy kutya vagyok, a nevem {self._nev}, a fajom {self.faj}.")

class Macska(Allat, Negylabu):
    faj = "makka"

    def __init__(self, nev, eletkor):
        super().__init__(nev)
        self._eletkor = eletkor
    def nyivak(self):
        print("Nyiff!")

    def nevetmond(self):
        print(f"Én egy macska vagyok, a nevem {self._nev}, a fajom {self.faj} és {self._eletkor} éves vagyok és a lábaim száma {self.LABAK_SZAMA}.")


bodri = Kutya("Bodrikutya")
bodri.nevetmond()
bodri.ugat()

cirmi = Macska("Huri", 17)
cirmi.nevetmond()
cirmi.nyivak()
