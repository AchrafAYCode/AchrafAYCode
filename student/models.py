from django.db import models 
from django.utils import timezone
from datetime import date

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from posts.models import Poste

class User(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    téléphone = models.CharField(max_length=8)
    email = models.EmailField(default='')

    def __str__(self):
        return self.nom + ' ' + self.prenom + ' ' + self.téléphone + ' ' + self.email 



class Réaction(models.Model):
    comment = models.TextField() 
    like = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    poste = models.ForeignKey(Poste, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.comment

class Recommandation(Poste): 
    text = models.CharField(max_length=50)

    def __str__(self):
        return self.text

class Transport(Poste):
    depart = models.CharField(max_length=50)
    destination = models.CharField(max_length=50) 
    heure_dep = models.DateTimeField(default=timezone.now)
    nbre_sièges = models.IntegerField()
    contactinfo = models.CharField(max_length=100) 

    def __str__(self):
        return 'Transport - ' + self.depart + ' à ' + self.destination

class Logement(Poste):
    localisation = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    contactinfo = models.CharField(max_length=100)

    def __str__(self):
        return 'Logement - ' + self.localisation


class Evénement(Poste):
    intitulé = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    lieu = models.CharField(max_length=50)
    contactInfo = models.CharField(max_length=50)

    def __str__(self):
        return 'Evénement - ' + self.intitulé

class EvenClub(Evénement):
    club = models.CharField(max_length=50)  

    def __str__(self): 
        return self.club + ' - ' + self.intitulé

class EvenSocial(Evénement):
    prix = models.FloatField()    

    def __str__(self): 
        return self.intitulé + ' - ' + str(self.prix)


# Create your models here.


    
