from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from django.urls import reverse_lazy
from .models import Poste ,Stage
from student.models import Recommandation,Transport  ,EvenSocial 
from django.views.generic import ListView , CreateView ,UpdateView
from .forms import  StageForm , RecommandationForm , TransportForm ,LogementForm,EvenClub,EvenSocialForm ,EvenClubForm
from django.shortcuts import redirect, get_object_or_404


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
        

class ListPostStage(ListView):
    model = Poste 
    template_name = 'listPosts/list_stages.html'
    form_class =  StageForm
    context_object_name = 'liste_stages' 
    
    
    
class ListPostTra(ListView):
    model = Poste 
    template_name = 'listPosts/list_transport.html'
    form_class =  TransportForm
    context_object_name = 'liste_transports' 
    
    
    
    
    
class ListPostRecommandation(ListView):
    model = Poste 
    template_name = 'listPosts/list_recommandation.html'
    form_class =  RecommandationForm
    context_object_name = 'liste_recommandation' 
    
    
    
class ListPostLogement(ListView):
    model = Poste 
    template_name = 'listPosts/liste_logement.html'
    form_class =  LogementForm
    context_object_name = 'liste_logement' 
    
    

class ListPostEvenementClub(ListView):
    model = Poste 
    template_name = 'listPosts/list_evenementClub.html'
    context_object_name = 'list_evenementClub'
    
class ListEvenementSocial(ListView):
    model = Poste 
    template_name = 'listPosts/list_evenementSocial.html'
    form_class =  EvenSocialForm
    context_object_name = 'list_evenementSocial' 
    

    
class ModifieStage(UpdateView):
    model = Stage
    template_name = 'modifPosts/modif_stage.html'
    form_class = StageForm
    context_object_name = 'modif_stage' 


class ModifierLogement(UpdateView):
    model = Poste
    template_name = 'modifPosts/modif_Logement.html'
    form_class = LogementForm
    context_object_name = 'modif_Logement' 

class ModifierRec(UpdateView):
    model = Recommandation
    template_name = 'modifPosts/modif_Rec.html'
    form_class = RecommandationForm
    context_object_name = 'modif_Rec' 

class ModifierTransport(UpdateView):
    model = Transport
    template_name = 'modifPosts/modif_Transport.html'
    form_class = TransportForm
    context_object_name = 'modif_Transport' 

class ModifierEvC(UpdateView):
    model = EvenClub
    template_name = 'modifPosts/modif_EvC.html'
    form_class = EvenClubForm
    context_object_name = 'modif_EvC' 

class ModifierEvS(UpdateView):
    model = EvenSocial
    template_name = 'modifPosts/modif_EvS.html'
    form_class = EvenClubForm
    context_object_name = 'modif_EvS'
    




def supprimer_Stage(request, poste_id):
    if request.method == 'POST':
        poste = get_object_or_404(Poste, id=poste_id)
        poste.delete()
        return redirect('liststage')
    

def supprimer_Logement(request, poste_id):
    if request.method == 'POST':
        poste = get_object_or_404(Poste, id=poste_id)
        poste.delete()
        return redirect('listLog')
   
def supprimer_Rec(request, poste_id):
    if request.method == 'POST':
        poste = get_object_or_404(Poste, id=poste_id)
        poste.delete()
        return redirect('listRecommandation')
   
     
def supprimer_Transport(request, poste_id):
    if request.method == 'POST':
        poste = get_object_or_404(Poste, id=poste_id)
        poste.delete()
        return redirect('listTransport')
  

def supprimer_EvS(request, poste_id):
    if request.method == 'POST':
        poste = get_object_or_404(Poste, id=poste_id)
        poste.delete()
        return redirect('listEvenS')
   
def supprimer_EvC(request, poste_id):
    if request.method == 'POST':
        poste = get_object_or_404(Poste, id=poste_id)
        poste.delete()
        return redirect('listEvenC')
    