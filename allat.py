class Allat:
    def __init__(self, nev):
        self._nev = nev

    def nevetmond(self):
        print(f"A nevem {self._nev}.")


class Kutya(Allat):
    faj = "puli"

    def ugat(self):
        print("Vuff!")

bodri = Kutya("Bodrikutya")

bodri.nevetmond()

bodri.ugat()