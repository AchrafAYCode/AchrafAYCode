from django.urls import path
from posts.views import ListePost , SelectFormView, CreerPostView 
urlpatterns = [
     path('', ListePost.as_view(), name='liste_posts'),
    path('creer_post/', SelectFormView.as_view(), name='select_form'),
    path('creer_post/<str:form_type>/', CreerPostView.as_view(), name='creer_post'),
]