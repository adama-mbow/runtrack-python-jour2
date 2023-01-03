def valeur(nombre):
    if nombre > 0:
        print("positif")
    elif nombre < 0:
        print("negatif")
nombre = int(input("entrer une valeur: "))
valeur(nombre)