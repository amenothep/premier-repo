# POO EXERCICE DE MISE EN SITUATION 4

# ---
class Personne:
    def __init__(self, nom : str):
        self.nom = nom

    def SePresenter(self):
        print("Bonjour, je m'appelle " + self.nom)

# ---


nombre_personne = int(input("nombre de personne"))

liste_personne = []
for i in range(nombre_personne):
    nom = input("nom de la personne " + str(i+1) + ":")
    liste_personne.append(Personne(nom))

for Personne in liste_personne:
    Personne.SePresenter()
