from django.db import models

# Create your models here.

class Livre(models.Model):
    STATUT_CHOICES = [
        ('disponible', 'Disponible'),
        ('emprunté', 'Emprunté'),
        ('réservé', 'Réservé'),
    ]

    id_livre = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=200)
    auteur = models.CharField(max_length=200)
    categorie = models.CharField(max_length=100)
    annee_publication = models.IntegerField()
    quantite_disponible = models.IntegerField()
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='disponible')

    def __str__(self):
        return self.titre
