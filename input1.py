inputresult2 = input("Írj be egy szövget: ")

print(inputresult2)
print(type(inputresult2))

inputresult = int(input('Írj be egy számot: '))


if not (isinstance(inputresult, int)):
    raise TypeError("Nem szám típusú amit beírtál.")
else:
    if inputresult<10:
        raise ValueError("10-nél nagyobb számot adj meg!")