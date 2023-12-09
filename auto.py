class Auto:

    def __init__(self):
        self._sebesseg = 0


    def get_sebesseg(self):
        print("Ez a getter.")
        return self._sebesseg

    def set_sebesseg(self, ujsebesseg):
        print("Ez a setter.")
        self._sebesseg = ujsebesseg

    sebesseg = property(get_sebesseg, set_sebesseg)

my_auto = Auto()

my_auto.sebesseg = 120
print(my_auto.sebesseg)