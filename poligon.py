class Poligon:
    def __init__(self, sides = 3, color = "piros"):
        self.sides = sides
        self.color = color
        self.oldalszelesseg = 2


my_poligon = Poligon(4, "zöld")
print(f"Ennek a poligonnak {my_poligon.sides} oldala van és a színe {my_poligon.color} és az oldalszélessége {my_poligon.oldalszelesseg}.")

my_poligon.sides = 3
print(f"Ennek a poligonnak {my_poligon.sides} oldala van és a színe {my_poligon.color} és az oldalszélessége {my_poligon.oldalszelesseg}.")