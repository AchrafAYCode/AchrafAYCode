from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from django.urls import reverse_lazy
from .models import Poste

from .forms import  StageForm , RecommandationForm , TransportForm ,LogementForm,EvenClubForm,EvenSocialForm


class ListePost(ListView):
    model = Poste
    template_name = 'mag/liste_posts.html'
    context_object_name = 'posts' 
    
    
class SelectFormView(View):
    template_name = 'mag/select_form.html'

    def get(self, request):
        return render(request, self.template_name)

class CreerPostView(View):
    template_name = 'mag/creer_posts.html'

    def get(self, request, form_type):
        form_classes = {
            'stage': StageForm,
            'transport': TransportForm,
            'recommandation': RecommandationForm,
            'logement': LogementForm,
            'evenement_club': EvenClubForm,
            'evenement_social': EvenSocialForm
        }
        form_class = form_classes.get(form_type)
        if form_class:
            return render(request, self.template_name, {'form': form_class()})
        

    def post(self, request, form_type):
        form_classes = {
            'stage': StageForm,
            'transport': TransportForm,
            'recommandation': RecommandationForm,
            'logement': LogementForm,
            'evenement_club': EvenClubForm,
            'evenement_social': EvenSocialForm
        }
        form_class = form_classes.get(form_type)
        if form_class:
            form = form_class(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse_lazy('liste_posts'))
            else:
                return render(request, self.template_name, {'form': form})
        
