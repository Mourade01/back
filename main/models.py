from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + "\n" + self.description
    
class KycInfo(models.Model):
    autheur = models.ForeignKey(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=200)
    nomFamille = models.CharField(max_length=200)
    sex = models.CharField(max_length=1)
    dateNaissance = models.DateField()
    lieuNaissance = models.CharField(max_length=200)
    dateExpiration = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)
    mkz = models.TextField()
    description = models.TextField()
    def __str__(self):
        return self.title + "\n" + self.description
