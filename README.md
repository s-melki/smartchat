# SmartChat Django CRUD

## Présentation

SmartChat est une application Django de gestion de bibliothèque (entité `Livre`) avec:
- CRUD complet (`Create`, `Read`, `Update`, `Delete`) via interface web
- Administration Django (`/admin/`)
- Intégration chatbot utilisant Ollama (`/livres/chatbot/`)
- Base de données MySQL

L’objet principal est le modèle `Livre` avec champs:
- `id_livre` (AutoField, primaire)
- `titre` (CharField)
- `auteur` (CharField)
- `categorie` (CharField)
- `annee_publication` (IntegerField)
- `quantite_disponible` (IntegerField)
- `statut` (CharField, choices: disponible/emprunté/réservé)

---

## Arborescence et description des fichiers

### dossiers principaux

- `smartchat/` : projet Django principal
- `livres/` : application métier (CRUD & chatbot)
- `venv/` : environnement virtuel (ne pas commiter)

### `smartchat/` (config projet)
- `settings.py` : configuration générale (apps installées, BDD MySQL, middleware, templates)
- `urls.py` : routes globales du projet (`admin/`, `livres/`)
- `wsgi.py` / `asgi.py` : points d’entrée serveurs

### `livres/` (app principale)
- `models.py` : modèle `Livre` et `STATUT_CHOICES`
- `admin.py` : enregistrement `admin.site.register(Livre)`
- `forms.py` : `LivreForm` (ModelForm) pour validation des formulaires
- `views.py` : contrôleurs
  - `livre_list` : liste tous les livres
  - `livre_add` : creation d’un livre
  - `livre_edit` : modification d’un livre
  - `livre_delete` : suppression d’un livre
  - `chatbot` : point d’accès chatbot (POST AJAX + template)
  - `generate_chatbot_response` : construit prompt et appelle Ollama
- `urls.py` : routes de l’app
  - `/` → `livre_list`
  - `/add/`, `/<id>/edit/`, `/<id>/delete/`, `/chatbot/`
- `templates/livres/` : pages HTML
  - `livre_list.html` : liste + liens CRUD + chatbot
  - `livre_form.html` : formulaire add/edit
  - `livre_confirm_delete.html` : confirmation suppression
  - `chatbot.html` : frontend chat simple JS + AJAX

### fichiers d’initialisation de données
- `populate_livres.py` : script de peuplement initial (50 livres de test)
- `add_hugo.py` : script d’ajout de 10 livres de Victor Hugo
- `populate_livres_complete.py` : script combiné (50 + 10 Hugo)

### autres
- `manage.py` : utilitaire Django (migrations, runserver…)

---

## Installation

1. Installer Python 3.12 (ou compatible)
2. Installer MySQL (et créer la DB `smartchat`)
3. Dans le projet:

```bash
cd /var/www/html/smartchat
python3 -m venv venv
source venv/bin/activate
pip install -U pip
pip install django mysqlclient requests
```

4. Installer dépendances système MySQL (Ubuntu):

```bash
sudo apt update
sudo apt install -y libmysqlclient-dev pkg-config
```

5. Configurer MySQL dans `smartchat/settings.py` :

```python
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'smartchat',
    'USER': 'root',
    'PASSWORD': 'Pass4root!',
    'HOST': 'localhost',
    'PORT': '3306',
  }
}
```

6. Appliquer migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

7. Créer un superuser:

```bash
DJANGO_SUPERUSER_USERNAME=test \
DJANGO_SUPERUSER_EMAIL=test@example.com \
DJANGO_SUPERUSER_PASSWORD=test \
python manage.py createsuperuser --noinput
```

8. Démarrer le serveur Django:

```bash
python manage.py runserver 127.0.0.1:8000
```

9. Accéder dans le navigateur:
- `http://127.0.0.1:8000/livres/`
- `http://127.0.0.1:8000/livres/chatbot/`
- `http://127.0.0.1:8000/admin/`

---

## Préparer Ollama (IA locale)

1. Installer Ollama:
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

2. Télécharger le modèle (ex: Mistral):
```bash
ollama pull mistral
```

3. Tester la requête:
```bash
curl -X POST http://localhost:11434/api/generate \
  -H 'Content-Type: application/json' \
  -d '{"model":"mistral","prompt":"Bonjour","stream":false}'
```

---

## Peupler la base de test

```bash
python populate_livres_complete.py
```

ou

```bash
python populate_livres.py
python add_hugo.py
```

---

## Fonctionnement du Chatbot

- Route: `POST /livres/chatbot/` (ou interface dans `/livres/chatbot/`)
- Reçoit `message` et construit `prompt` à partir de la table `Livre`
- Appelle Ollama API locale `http://localhost:11434/api/generate`
- Renvoie JSON `{ "response": "..." }`

### Exemple de question
- `Est-ce que le livre avec l'ID 102 existe ?`
- `Le roman Les Misérables est-il disponible ?`
- `Je veux un roman romantique facile à lire.`
- `Je cherche un livre de Victor Hugo.`

---

## Notes supplémentaires

- Ce projet est fait pour développement et test. Ne jamais utiliser `DEBUG=True` en production.
- Protéger les secrets avec variables d'environnement (`SECRET_KEY`, DB credentials).
- Amélioration possible: ajouter champs `date_retour_prevue` / `emprunteur`, pagination, recherche, authentification.
# smartchat
