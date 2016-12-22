from random import *

def shake(mot):
    liste = []
    listt = []
    for i in range(len(mot)):
        liste.append(i)
        listt.append(i)
    for i in mot:
        j = choice(liste)
        listt[j] = i
        liste.remove(j)
    print (''.join(listt))
        
shake(input("Mot:"))
