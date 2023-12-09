class Poligon:
    color = "piros"
    def __init__(self, sides):
        self.sides = sides
        self._oldalszelesseg = 2

    def getoldalszelesseg(self):
        return self._oldalszelesseg

    def __str__(self):
        return "Én egy poligon vagyok."


my_poligon = Poligon(4)

print(my_poligon.getoldalszelesseg())
print(my_poligon)
