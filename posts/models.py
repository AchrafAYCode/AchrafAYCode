from django.db import models
from datetime import date
from django.contrib.auth.models import User
# Create your models here.

class Poste(models.Model): 
    TYPE_CHOICES = [('0', 'offre'), ('1', 'demande')]
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    date = models.DateField(null=True, default=date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.get_type_display() + ' - ' + str(self.date)



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