class Etel:

    def __init__(self):
        self._nev = ""
        self._ar = 0

    def get_ar(self):
        return self._ar

    def set_ar(self, ar):
        if ar < 0 or ar > 100000:
            print("Nem megfelelő ár!")
        else:
            self._ar = ar


    def get_nev(self):
        return self._nev


    def set_nev(self, ujnev):
        self._nev = ujnev


class Restaurant:
    def __init__(self, menuitems, etteremnev):
        self.menuitems = menuitems
        self.etteremnev = etteremnev

    def __str__(self):
        return f"Az étterem neve {self.etteremnev}"


    def __add__(self, other):
        self.menuitems.append(other)
    def getmenuitems(self):
        for menuitem in self.menuitems:
            print(f"{menuitem.get_nev()}................{menuitem.get_ar()} Ft")

my_restaurant = Restaurant([],"Kisbojtár")
my_restaurant.getmenuitems()

for i in range(2):
    etel_neve = input("Add meg az étel nevét: ")
    etel_ara = int(input("Add meg az étel árát: "))
    etel_uj = Etel()
    etel_uj.set_nev(etel_neve)
    etel_uj.set_ar(etel_ara)
    my_restaurant + etel_uj


my_restaurant.getmenuitems()

print(my_restaurant)