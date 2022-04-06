class personne:
    def __init__(self, nom: str = "", age: int = 0):
        self.nom = nom
        self.age = age
        if self.nom == "":
            self.demandernom()
        print("constructeur " + self.nom)
    def sepresenter(self):
        if self.age == 0:
            print("bonjour je m'appele " + self.nom)
        else:
            print("bonjour je m'appele " + self.nom + "et mon age est : " + str(self.age) + " ans")
            if self.estmajeur():
                print ("je suis majeur")
            else :
                print("je suis mineur")

    def estmajeur(self):
        return self.age >= 18

    def demandernom(self):
        self.nom = input("quel est votre nom ? ")

personne1 = personne("toto", 10)
personne1.sepresenter()


personne2 = personne("titi", 30)
personne2.sepresenter()

personne3 =personne("", 30)
personne3.sepresenter()