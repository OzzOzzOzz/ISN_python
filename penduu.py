#################################################
#var init
prop = []
mott = ""
#################################################
#def
def prompt (prop):
    while 1:
        print("")
        print("Lettres déjà proposées :",prop)
        print("Lettres déjà proposées : ",res)
        lettre = str(input("Proposition de lettre :"))
    
        if lettre in prop:
            print("Vous avez déjà proposé cette lettre \n")
        elif len(lettre) != 1:
            print("une seule lettre por favor")
        else:
            break

    prop.append(lettre.upper())
    return lettre.upper()

def resdef(mot):
    res = ""
    for i in range(len(mot)):
        res = res + "-"
    return res

def resfill(res,lettre,mot,):
    listt = []
    j = 0
    while





    
    ress= ""
    for i in range(len(res)):
        if

        
    return ress
#################################################
#RUN
mot = str(input("Mot a deviner :")).upper()
print("Votre mot est ",mot)
input("PRESS ENTER TO CONTINUE")
for i in range(100):
    print("  ")
res = resdef(mot)
while mot != mott:
    lettre = prompt(prop)

