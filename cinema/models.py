from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class Utilisateur(AbstractUser):

    def __str__(self):
        return self.username 

class Categorie(models.Model):
    libelle = models.CharField(max_length=200, null=False)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('-created_at',)
    
    def __str__(self):
        return f'{self.libelle} {self.id}' 




class Films(models.Model):
    titre = models.CharField(max_length=200, null=False) 
    description = models.CharField(max_length=200, null= False)
    version = models.CharField(max_length=200, null=False)
    prix = models.IntegerField(default=0) 
    image = models.ImageField(upload_to="Films/",null=False, blank=False)
    auteur = models.CharField(max_length=200, null = False)
    # horaire_dep_diff = models.DateTimeField()
    # horaire_fin_diff = models.DateTimeField()
    horaire_diff = models.DateTimeField()
    Categorie = models.ForeignKey(Categorie, on_delete = models.CASCADE) 
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('-created_at',)
    
    def __str__(self):
        return f'{self.titre}' 


class Ticket(models.Model):
    numero = models.IntegerField(default=1)
    films = models.ForeignKey(Films, on_delete = models.CASCADE) 
    user = models.ForeignKey(Utilisateur, on_delete = models.CASCADE)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('-created_at',)
    
    def __str__(self):
        return f'{self.numero}'


class Place(models.Model):
    numPlace = models.IntegerField(default = 1)
    ticket = models.ForeignKey(Ticket, on_delete = models.CASCADE)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('-created_at',)
    
    def __str__(self):
        return f'{self.numPlace}'


class Salle(models.Model):
    nom = models.CharField(max_length=200, null = False)
    lieu = models.CharField(max_length=200, null = False)
    place = models.ForeignKey(Place, on_delete = models.CASCADE)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('-created_at',)
    
    def __str__(self):
        return f'{self.nom}'
