def triangle(a,b,c):
    if (a < (b+c)) or (b < (a+c)) or (c <(a+b)):
        print("ces trois longueur détermine une triangle.")
    else:
        print("on ne peut pas construire une triangle aves ces longueurs.")
    if (a==b) and (b==c):
        return("on a une triangle équilaterale")
    elif ((a == b) or (b == a) or (c == a)) and ((a*a + b*b ==round(c*c)) or (b*b +c*c == round(a*a)) or (c*c + a*a == round(b*b))):
        return("on a une triangle rectangle et isocèle")
    elif (a == b) or (b == a) or (c == a):
        return ("on a une triangle isocele")
    elif (a*a + b*b ==round(c*c)) or (b*b +c*c ==round(a*a)) or (c*c + a*a == round(b*b)):
        return("on a une triangle rectangle")
    else:
        return("on a une triangle quelconque")
a = int(input("mettez la valeur de a. "))
b = int(input("mettez la valeur de b. "))
c = int(input("mettez.  la valeur de c. "))
print(triangle(a,b,c))