class Poligon:
    def __init__(self, sides = 3, color = "piros"):
        self.sides = sides
        self.color = color
        self.oldalszelesseg = 2


my_poligon = Poligon(4, "zöld")
print(f"Ennek a poligonnak {my_poligon.sides} oldala van és a színe {my_poligon.color} és az oldalszélessége {my_poligon.oldalszelesseg}.")

your_poligon = Poligon(3, "kék")
print(f"Ennek a poligonnak {your_poligon.sides} oldala van és a színe {your_poligon.color} és az oldalszélessége {your_poligon.oldalszelesseg}.")

third_poligon = Poligon(5)
print(f"Ennek a poligonnak {third_poligon.sides} oldala van és a színe {third_poligon.color} és az oldalszélessége {third_poligon.oldalszelesseg}.")