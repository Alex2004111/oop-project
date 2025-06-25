class Livre:
    def __init__(self, titre, auteur, isbn, date_ajout):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn
        self.date_ajout = date_ajout
        self.disponible = True
        self.nb_emprunts = 0

    def afficher_info(self):
        print(f"{self.titre} par {self.auteur} | ISBN: {self.isbn} | Disponible: {self.disponible} | Emprunts: {self.nb_emprunts}")

    def emprunter(self):
        if self.disponible:
            self.disponible = False
            self.nb_emprunts += 1
            return True
        return False

    def retourner(self):
        self.disponible = True