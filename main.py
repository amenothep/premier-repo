def demandernom():
    nom = ""
    while nom == "":
        nom = input("quel est ton nom ? ")
        if nom == "": print("merci de rentrer un nom en lettre")
    return nom
def demanderprenom(nomperson):
    prenom = ""
    while prenom == "":
        prenom = input(nomperson + "quel est ton prenom ? ")
        if prenom == "": print(nomperson + "merci de rentrer le prenom en lettre")
    return prenom

def demanderage (nomperson):
    age = 0
    while age == 0:
        agestr = input(nomperson + "quel est ton age ? ")
        try:
            age = int(agestr)
        except:
            print(nomperson + ";erci de rentrer votre qge en nu;eriaue")
    return age


def afficherinfopersonne(nom, prenom, age):
    print("le user est : " + nom + " " + prenom + ". et son age est : " + str(age) + " ans")
    print("l'an prochain, t'aura " + str(age + 1) + " ans")
    if age == 1 or age == 2 or age==3:
        print("vous etes bebe")
    elif 3 < age > 17 :
        print("vous etes enfant")
    elif age == 17:
        print("vous etes presque majeur")
    elif age == 18:
        print("vous etes tout just majeur")
    elif age <= 18:
        print("vous etes mineur")
    elif age >= 18:
        print("vous etes  majeur")


nomm1 = demandernom()
nomm2 = demandernom()
prenomm1 = demanderprenom(nomm1)
prenomm2 = demanderprenom(nomm2)
agee1 = demanderage(nomm1)
agee2 = demanderage(nomm2)
afficherinfopersonne(nomm1, prenomm1, agee1)
afficherinfopersonne(nomm2, prenomm2, agee2)

print(agee1, 20, agee2, "toto")


"""
n = 0
while n < 10:
    print ("vqleur de n est : " + str(n))
    n = n + 1
print("sortie")
"""