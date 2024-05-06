from django.contrib import admin
from .models import User, Poste, Réaction, Recommandation, Transport, Logement, Evénement, EvenClub, EvenSocial

admin.site.register(User)
admin.site.register(Réaction)
admin.site.register(Recommandation)
admin.site.register(Transport)
admin.site.register(Logement)
admin.site.register(Evénement)
admin.site.register(EvenClub)
admin.site.register(EvenSocial)
