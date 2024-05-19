from django.contrib.auth.models import User
from django.urls import reverse_lazy 
from posts.forms import PostForm
from posts.models import Poste 
from django.views.generic import DeleteView
from django.shortcuts import get_object_or_404, redirect, render





class SupprimerPost(DeleteView):
    model = Poste
    template_name = 'supprimer_Poste.html'
    success_url = reverse_lazy('user_profil')

    def get_success_url(self):
        user_id = self.object.user.id
        return reverse_lazy('user_profil', kwargs={'user_id': user_id})


def user_profil(request, user_id): 
    user = get_object_or_404(User, pk=user_id)
    user_posts = Poste.objects.filter(user=user)
    return render(request, 'user_profil.html', {'user': user, 'posts': user_posts})




def modifier_poste(request, user_id, poste_id):
    poste = get_object_or_404(Poste, pk=poste_id)
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=poste)
        if form.is_valid():
            form.save()
            return redirect('user_profil', user_id=poste.user.id)
    else:
        form = PostForm(instance=poste)
    return render(request, 'modifier_poste.html', {'form': form})



