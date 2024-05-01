from django.db import models 
from django.utils import timezone
from datetime import date
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class User(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    téléphone = models.CharField(max_length=8)
    email = models.EmailField(default='')

    def __str__(self):
        return self.nom + ' ' + self.prenom + ' ' + self.téléphone + ' ' + self.email 


class Poste(models.Model): 
    TYPE_CHOICES = [('0', 'offre'), ('1', 'demande')]
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    date = models.DateField(null=True, default=date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.get_type_display() + ' - ' + str(self.date)

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

class Stage(Poste):
    TYPE_CHOICES = [('1', 'ouvrier'), ('2', 'technicien'), ('3', 'pfe')]
    typeStg = models.CharField(max_length=1, choices=TYPE_CHOICES)
    société = models.CharField(max_length=50) 
    durée = models.IntegerField()
    sujet = models.CharField(max_length=50)
    contactinfo = models.CharField(max_length=50)
    spécialite = models.CharField(max_length=255, choices=TYPE_CHOICES, default='')

    def __str__(self): 
        return 'Stage - ' + self.société + ' - ' + self.sujet

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


    
