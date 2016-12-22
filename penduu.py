prop = [ "a" , "d" , "e" ]
def prompt (prop):
    while 1:
        print("Lettre déjà proposées :",prop)
        lettre = str(input("Proposition de lettre :"))
    
        if lettre in prop:
            print("Vous avez déjà proposé cette lettre \n")
        elif len(lettre) != 1:
            print("une seule lettre por favor\n")
        else:
            break

    prop.append(lettre)
    return lettre.lower()
    
lettre = prompt(prop)
