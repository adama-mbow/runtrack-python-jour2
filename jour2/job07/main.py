def langage(x):
    resultat = (x)
    if resultat == "javascript":
        print("tu es un developpeur web")
    elif resultat == "python":
        print("tu es un développeur IA")
    elif resultat == "java":
        print("tu es un développeur logiciel")
    elif resultat == "reactjs":
        print("tu es un developpeur mobile")
    else:
        print("un jour, je serai le meilleur developpeur...")
resultat = input("quel est ton langage préféré ? ")
langage(resultat)