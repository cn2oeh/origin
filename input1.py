inputresult = int(input("Írj be egy szövget: "))


if not (isinstance(inputresult, int)):
    raise TypeError("Nem szám típusú amit beírtál.")
else:
    if inputresult<10:
        raise ValueError("10-nél nagyobb számot adj meg!")
