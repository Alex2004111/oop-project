from collections import deque
from models.reservation import Reservation

class Bibliotheque:
    def __init__(self, nom):
        self.nom = nom
        self.livres = {}  # isbn: Livre
        self.utilisateurs = {}  # id: Utilisateur
        self.reservations = {}  # isbn: deque()

    def ajouter_livre(self, livre):
        self.livres[livre.isbn] = livre

    def supprimer_livre(self, isbn):
        self.livres.pop(isbn, None)

    def enregistrer_utilisateur(self, utilisateur):
        self.utilisateurs[utilisateur.id] = utilisateur

    def rechercher_livres(self, mot_cle):
        return [livre for livre in self.livres.values() if mot_cle.lower() in livre.titre.lower()]

    def emprunter_livre(self, utilisateur_id, isbn):
        utilisateur = self.utilisateurs.get(utilisateur_id)
        if utilisateur:
            utilisateur.emprunter_livre(self, isbn)

    def retourner_livre(self, utilisateur_id, isbn):
        utilisateur = self.utilisateurs.get(utilisateur_id)
        if utilisateur:
            utilisateur.retourner_livre(self, isbn)
            # Vérifie les réservations
            if isbn in self.reservations and self.reservations[isbn]:
                prochain = self.reservations[isbn].popleft()
                print(f"Notification: le livre est maintenant disponible pour {prochain.utilisateur.nom}.")

    def reserver_livre(self, utilisateur_id, isbn):
        utilisateur = self.utilisateurs.get(utilisateur_id)
        livre = self.livres.get(isbn)
        if utilisateur and livre:
            self.reservations.setdefault(isbn, deque()).append(Reservation(utilisateur, livre))

    def afficher_catalogue(self):
        for livre in self.livres.values():
            livre.afficher_info()

    def afficher_statistiques(self):
        top = sorted(self.livres.values(), key=lambda l: l.nb_emprunts, reverse=True)[:5]
        print("Top 5 livres les plus empruntés:")
        for livre in top:
            print(f"{livre.titre} ({livre.nb_emprunts} emprunts)")
        total = sum(1 for l in self.livres.values() if not l.disponible)
        print(f"Emprunts actifs: {total}")
