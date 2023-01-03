def production(type, saison):
    if type == "fruit" and saison == "hiver":
        return("orange, mandarine et kiwi")
    elif type == "fruit" and saison =="été":
        return ("poire, fraise, sassis")
    elif type =="legume" and saison =="hiver":
        return("carotte, topinambour, endive")
    elif type == "legume" and saison == "été":
        return("artichaut, aubergine, navet")
    else: 
        return("opps!! vérifier ce que vous avez écrit !")
type = input("entre fruit et legume, quel est le type de nourriture aimeriez-vous manger ? ")
saison = input("vous préfèriez le manger durant quelle période ? ")
print(production(type, saison))
    