class Etel:

    def __init__(self, nev, ar):
        self.nev = nev
        self.ar = ar

class Restaurant:
    def __init__(self, menuitems, etteremnev):
        self.menuitems = menuitems
        self.etteremnev = etteremnev

    def __str__(self):
        return f"Az éltterem neve {self.etteremnev}"


    def __add__(self, other):
        self.menuitems.append(other)
    def getmenuitems(self):
        for menuitem in self.menuitems:
            print(f"{menuitem.nev}................{menuitem.ar} Ft")

etel1 = Etel('Hambi', 100)
etel2 = Etel('Hotdog', 150)
my_menu = [etel1, etel2]

my_restaurant = Restaurant(my_menu,"Kisbojtár")
my_restaurant.getmenuitems()

for i in range(2):
    etel_neve = input("Add meg az étel nevét: ")
    etel_ara = int(input("Add meg az étel árát: "))
    if etel_ara < 0 or etel_ara > 100000:
        print("Nem megfelelő ár!")
        break
    else:
        my_restaurant + Etel(etel_neve, etel_ara)

my_restaurant.getmenuitems()

print(my_restaurant)