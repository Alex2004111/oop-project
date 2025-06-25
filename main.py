from models.bibliotheque import Bibliotheque 
from models.livre import Livre
from models.utilisateur import Utilisateur


biblio = Bibliotheque("Bibliothèque Centrale")


dl = [
    Livre("1984", "George Orwell", "001", "2023-01-01"),
    Livre("Python 101", "Michael Driscoll", "002", "2023-01-05")
]
for livre in dl:
    biblio.ajouter_livre(livre)


u1 = Utilisateur(1, "Adam")
biblio.enregistrer_utilisateur(u1)



while True:
    print("\n===== MENU =====")
    print("1. Afficher catalogue")
    print("2. Emprunter livre")
    print("3. Retourner livre")
    print("4. Réserver")
    print("5. Statistiques")
    print("6. Ajouter livre")
    print("7. Supprimer livre")
    print("8. Quitter")

    choix = input("Choix: ")

    if choix == "1":
        biblio.afficher_catalogue()

    elif choix == "2":
        isbn = input("ISBN à emprunter: ")
        biblio.emprunter_livre(1, isbn)

    elif choix == "3":
        isbn = input("ISBN à retourner: ")
        biblio.retourner_livre(1, isbn)

    elif choix == "4":
        isbn = input("ISBN à réserver: ")
        biblio.reserver_livre(1, isbn)

    elif choix == "5":
        biblio.afficher_statistiques()

    elif choix == "6":
        titre = input("Titre du livre: ")
        auteur = input("Auteur: ")
        isbn = input("ISBN (unique): ")
        date = input("Date d'ajout (YYYY-MM-DD): ")
        livre = Livre(titre, auteur, isbn, date)
        biblio.ajouter_livre(livre)
        print("✅ Livre ajouté.")

    elif choix == "7":
        isbn = input("ISBN du livre à supprimer: ")
        biblio.supprimer_livre(isbn)
        print("📕 Livre supprimé (si existant).")

    elif choix == "8":
        print("👋 Au revoir !")
        break

    else:
        print("⛔ Choix invalide.")
