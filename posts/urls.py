from django.urls import path
from posts import views
from profil import views
from posts.views import ListePost , SelectFormView, CreerPostView ,ListPostRecommandation,ListPostTra,ListPostEvenementClub,ListPostLogement,ListEvenementSocial,ListPostStage,ModifierPost
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
    path('<int:pk>/modifier/', ModifierPost.as_view(),name='modifier_stage'),
    path('user/<int:user_id>/', views.user_profile_view, name='user_profile'),
    
]