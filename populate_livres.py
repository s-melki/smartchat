import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smartchat.settings')
django.setup()

from livres.models import Livre

# Common helper

def create_livre(titre, auteur, categorie, annee_publication, quantite_disponible, statut):
    Livre.objects.create(
        titre=titre,
        auteur=auteur,
        categorie=categorie,
        annee_publication=annee_publication,
        quantite_disponible=quantite_disponible,
        statut=statut,
    )

# 1) Create 50 sample books with varied titles/authors

titres = [
    "Le Petit Prince", "1984", "Harry Potter à l'école des sorciers", "To Kill a Mockingbird",
    "The Great Gatsby", "Pride and Prejudice", "The Catcher in the Rye", "Lord of the Flies",
    "Animal Farm", "Brave New World", "The Hobbit", "The Lord of the Rings", "Alice's Adventures in Wonderland",
    "The Adventures of Huckleberry Finn", "Moby-Dick", "War and Peace", "Crime and Punishment",
    "The Brothers Karamazov", "Don Quixote", "Ulysses", "One Hundred Years of Solitude",
    "The Sound and the Fury", "In Search of Lost Time", "The Trial", "The Castle",
    "Madame Bovary", "Anna Karenina", "The Awakening", "The Age of Innocence", "Ethan Frome",
    "The House of Mirth", "The Custom of the Country", "The Reef", "The Spoils of Poynton",
    "What Was She Thinking?", "The Buccaneers", "The Glimpses of the Moon", "The Children",
    "The Mother's Recompense", "Hudson's Group", "The Old Maid", "The Spark", "The Pretext",
    "The Gods Arrive", "The Last of the Duchess", "The Penitent", "The Head of the House of Coombe",
    "The Fruit of the Tree", "The Custom of the Country (play)", "The Glimpses of the Moon (play)"
]

auteurs = [
    "Antoine de Saint-Exupéry", "George Orwell", "J.K. Rowling", "Harper Lee",
    "F. Scott Fitzgerald", "Jane Austen", "J.D. Salinger", "William Golding",
    "George Orwell", "Aldous Huxley", "J.R.R. Tolkien", "J.R.R. Tolkien", "Lewis Carroll",
    "Mark Twain", "Herman Melville", "Leo Tolstoy", "Fyodor Dostoevsky",
    "Fyodor Dostoevsky", "Miguel de Cervantes", "James Joyce", "Gabriel García Márquez",
    "William Faulkner", "Marcel Proust", "Franz Kafka", "Franz Kafka",
    "Gustave Flaubert", "Leo Tolstoy", "Kate Chopin", "Edith Wharton", "Edith Wharton",
    "Edith Wharton", "Edith Wharton", "Edith Wharton", "Edith Wharton",
    "Edith Wharton", "Edith Wharton", "Edith Wharton", "Edith Wharton",
    "Edith Wharton", "Edith Wharton", "Edith Wharton", "Edith Wharton", "Edith Wharton",
    "Edith Wharton", "Edith Wharton", "Edith Wharton", "Edith Wharton",
    "Edith Wharton", "Edith Wharton", "Edith Wharton"
]

categories = ["Fiction", "Science Fiction", "Fantasy", "Classics", "Romance", "Mystery", "Thriller", "Biography"]

statuts = ["disponible", "emprunté", "réservé"]

print("Création de 50 livres d'exemple...")
for i in range(50):
    titre = titres[i % len(titres)]
    auteur = auteurs[i % len(auteurs)]
    categorie = categories[i % len(categories)]
    annee_publication = 1900 + (i % 121)  # Années 1900-2020
    quantite_disponible = (i % 10) + 1
    statut = statuts[i % len(statuts)]

    if i < len(titres):
        final_title = titre
    else:
        final_title = f"{titre} #{i + 1}"

    create_livre(final_title, auteur, categorie, annee_publication, quantite_disponible, statut)

print("50 livres créés.")

# 2) Ajouter 10 livres de Victor Hugo

hugo_books = [
    "Les Misérables",
    "Notre-Dame de Paris",
    "Les Travailleurs de la mer",
    "Quatrevingt-treize",
    "L'Homme qui rit",
    "Les Châtiments",
    "La Légende des siècles",
    "Hernani",
    "Ruy Blas",
    "Les Contemplations"
]

print("Ajout de 10 livres de Victor Hugo...")
for i, title in enumerate(hugo_books):
    create_livre(title, "Victor Hugo", "Classics", 1860 + i, 5, "disponible")

print("10 livres de Victor Hugo ajoutés.")