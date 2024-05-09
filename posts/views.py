from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from django.urls import reverse_lazy
from .models import Poste
from django.views.generic import ListView , CreateView ,UpdateView
from .forms import  StageForm , RecommandationForm , TransportForm ,LogementForm,EvenClub,EvenSocialForm



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
            'evenement_club': EvenClub,
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
            'evenement_club': EvenClub,
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
        

class ListPostStage(ListView):
    model = Poste 
    template_name = 'listPosts/list_stages.html'
    form_class =  StageForm
    context_object_name = 'liste_stages' 
    
    
    
class ListPostTra(CreateView):
    model = Poste 
    template_name = 'listPosts/list_transport.html'
    form_class =  TransportForm
    context_object_name = 'liste_transports' 
    
    
    
    
    
class ListPostRecommandation(CreateView):
    model = Poste 
    template_name = 'listPosts/list_recommandation.html'
    form_class =  RecommandationForm
    context_object_name = 'liste_recommandation' 
    
    
    
class ListPostLogement(CreateView):
    model = Poste 
    template_name = 'listPosts/liste_logement.html'
    form_class =  LogementForm
    context_object_name = 'liste_logement' 
    
    

class ListPostEvenementClub(CreateView):
    model = Poste 
    template_name = 'listPosts/list_evenementClub.html'
    form_class =  EvenClub
    context_object_name = 'list_evenementClub' 
    
class ListEvenementSocial(CreateView):
    model = Poste 
    template_name = 'listPosts/list_evenementSocial.html'
    form_class =  EvenSocialForm
    context_object_name = 'list_evenementSocial' 
    


class ModifierPost(UpdateView):
    model = Poste
    template_name = 'modifPosts/modif_stage.html'
    form_class = StageForm
    context_object_name = 'modif_stage' 
    
