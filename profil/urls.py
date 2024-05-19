from django.urls import path
from profil import views
urlpatterns = [
    path('user/<int:user_id>/', views.user_profile_view, name='user_profile'),
    path('user/<int:user_id>/posts/', views.user_posts_view, name='user_posts'),

]