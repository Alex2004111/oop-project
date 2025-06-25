# 📖 Projet Python POO - Système de gestion de bibliothèque

Ce projet est une application en Python utilisant la **programmation orientée objet (POO)** pour simuler la gestion d'une bibliothèque. Il comprend la gestion des livres, des utilisateurs, des emprunts, des réservations, et des statistiques.

---

## ⚡ Fonctionnalités principales

* Ajouter et supprimer des livres
* Enregistrer des utilisateurs
* Emprunter et retourner des livres
* Réserver un livre indisponible (file d'attente)
* Limiter à 3 emprunts par utilisateur
* Gérer les retards et pénalités
* Afficher des statistiques : livres les plus empruntés, emprunts actifs, etc.

---

## 🔧 Technologies utilisées

* Python 3
* Programmation orientée objet (classes, héritage, encapsulation)
* Console (interface texte)

---

## 🏢 Structure du projet

```
poo-project/
├── main.py                     # Interface console
├── models/
│   ├── livre.py              # Classe Livre
│   ├── utilisateur.py        # Classe Utilisateur
│   ├── bibliotheque.py        # Classe Bibliotheque
│   └── reservation.py         # Classe Reservation
```

---

## 🏆 Répartition du travail (par étudiants)

| Étudiant    | Tâche principale                                                        |
| ----------- | ----------------------------------------------------------------------- |
| **Adam**    | Interface console (`main.py`), menu interactif et liaison entre classes |
| **Zaid**    | Classe `Livre` (emprunt, retour, info)                                  |
| **Hamza**   | Classe `Utilisateur` (limites, pénalités, historique)                   |
| **Hatim**   | Classe `Bibliotheque` (catalogue, recherche, statistiques)              |
| **Mohamed** | Classe `Reservation` (file d'attente, messages de confirmation)         |

---

## 🔄 Exemple d'utilisation (menu)

```bash
1. Afficher catalogue
2. Emprunter livre
3. Retourner livre
4. Réserver
5. Statistiques
6. Ajouter livre
7. Supprimer livre
8. Quitter
```

---

## 📅 Date de réalisation

> Juin 2025, dans le cadre du module de Programmation Orientée Objet (POO).

---

## ✅ Auteurs

Projet réalisé par : **Adam, Zaid, Hamza, Hatim, Mohamed**
