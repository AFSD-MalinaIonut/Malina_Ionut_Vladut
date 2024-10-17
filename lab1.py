
articol = """
Cazul dispariției copiilor milionarului din Hunedoara se complică tot mai mult. Adrian Marțian vrea să îi ducă pe cei 3 minori în Rusia, potrivit surselor Antena 3 CNN. Acesta i-ar fi găsit pe micuți, miercuri noaptea, în apropiere de Dunăre, iar acum s-ar afla deja în Serbia.
În data de 13 Octombrie, duminică, la ora 11:30, minorii au fost văzuți într-0 benzinărie, alături de un bărbat, într-un Mercedes alb cu numere de Cluj, precizează aceleași surse citate. Mașina ar fi a lui Adrian Marțian.

Pe data de 14 Octombrie, aceeași mașină a fost văzută din nou, dar erau condusă de un alt bărbat. Copiii nu mai erau în mașină.
 """


lungime = len(articol)
if lungime % 2 == 0:
    parte1 = articol[:lungime // 2]
    parte2 = articol[lungime // 2:]
else:
    parte1 = articol[:lungime // 2 + 1]
    parte2 = articol[lungime // 2 + 1:]


parte1 = parte1.strip().upper()


parte2 = parte2[::-1]
parte2 = parte2.capitalize()
parte2 = ''.join(char for char in parte2 if char.isalnum() or char.isspace())


rezultat = parte1 + ' ' + parte2


print(rezultat)
