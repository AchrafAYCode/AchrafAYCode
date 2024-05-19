from django.urls import path
from profil.views import modifier_poste,  user_profil
from profil import views

urlpatterns = [
    path('user/<int:user_id>/', user_profil, name='user_profil'),
    path('user/<int:user_id>/poste/<int:poste_id>/modifier/', modifier_poste, name='modifier_poste'),
    path('<int:pk>/supprimer/', views.SupprimerPost.as_view(), name='SupprimerPost'),

]