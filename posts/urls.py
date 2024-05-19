from django.urls import path
from posts import views
from profil import views
from .views import ModifieStage ,ModifierLogement,ModifierRec,ModifierEvC,ModifierTransport,ModifierEvS
from posts.views import ListePost , SelectFormView, CreerPostView ,ListPostRecommandation,ListPostTra,ListPostEvenementClub,ListPostLogement,ListEvenementSocial,ListPostStage, supprimer_EvC, supprimer_EvS, supprimer_Logement, supprimer_Rec, supprimer_Stage, supprimer_Transport
urlpatterns = [
     path('', ListePost.as_view(), name='liste_posts'),
    path('creer_post/', SelectFormView.as_view(), name='select_form'),
    path('creer_post/<str:form_type>/', CreerPostView.as_view(), name='creer_post'),
    path('liste_stage/',ListPostStage.as_view(), name='liststage'),
    path('liste_recommandation/',ListPostRecommandation.as_view(), name='listRecommandation'),
    path('liste_evenementClub/',ListPostEvenementClub.as_view(), name='listEvenC'),
    path('liste_transport/',ListPostTra.as_view(), name='listTransport'),
    path('liste_logement/',ListPostLogement.as_view(), name='listLog'),
    path('liste_evenementSocial/',ListEvenementSocial.as_view(), name='listEvenS'),
    path('<int:pk>/modif_stage/',ModifieStage.as_view(),name='modif_stage'),
     path('<int:pk>/modif_Logement/', ModifierLogement.as_view(),name='modif_Logement'),
     path('<int:pk>/modif_Rec/', ModifierRec.as_view(),name='modif_Rec'),
     path('<int:pk>/modif_EvC/', ModifierEvC.as_view(),name='modif_EvC'),
     path('<int:pk>/modif_EvS/', ModifierEvS.as_view(),name='modif_EvS'),
     path('<int:pk>/modif_Transport/', ModifierTransport.as_view(),name='modif_Transport'),
    path('supprimer_Stage/<int:poste_id>/', supprimer_Stage, name='supprimer_Stage'),
    path('supprimer_Logement/<int:poste_id>/', supprimer_Logement, name='supprimer_Logement'),
    path('supprimer_Rec/<int:poste_id>/', supprimer_Rec, name='supprimer_Rec'),
     path('supprimer_Transport/<int:poste_id>/', supprimer_Transport, name='supprimer_Transport'),
     path('supprimer_EvS/<int:poste_id>/', supprimer_EvS, name='supprimer_EvS'),
     path('supprimer_EvC/<int:poste_id>/', supprimer_EvC, name='supprimer_EvC'),
    
]