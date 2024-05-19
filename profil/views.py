from django.contrib.auth.models import User 
from posts.models import Poste 
from django.shortcuts import get_object_or_404, render


def user_profile_view(request, user_id):
    user_instance = get_object_or_404(User, pk=user_id)
    user_posts = Poste.objects.filter(user=user_instance)
    return render(request, 'userProfile.html', {'user': user_instance, 'user_posts': user_posts})

from django.contrib.auth.decorators import login_required
@login_required()
def user_posts_view(request, user_id):
    user_instance = User.objects.get(pk=user_id)
    posts = Poste.objects.filter(user=user_instance)
    return render(request, 'user_posts.html', {'user': user_instance, 'posts': posts})
# Create your views here.
