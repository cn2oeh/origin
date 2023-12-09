class Poligon:
    color = "piros"
    def __init__(self, sides):
        self.sides = sides
        self.oldalszelesseg = 2


my_poligon = Poligon(4)
print(f"Ennek a poligonnak {my_poligon.sides} oldala van és a színe {my_poligon.color}.")

my_triangle = Poligon(3)
print(f"Ennek a poligonnak {my_triangle.sides} oldala van és a színe {my_triangle.color}.")

Poligon.color="kék"
print(f"My_poligon poligonnak {my_poligon.sides} oldala van és a színe {my_triangle.color}.")
