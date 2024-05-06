from django.forms import ModelForm 
from .models import Poste  , Recommandation ,Transport ,Logement  ,Evénement ,EvenClub ,EvenSocial 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django import forms 

class PosteForm(ModelForm): 
    class Meta : 
        model=Poste 
        fields="__all__" 
        
class RecommandationForm(ModelForm): 
    class Meta : 
        model=Recommandation 
        fields="__all__"
        
        
class TransportForm(ModelForm): 
    class Meta : 
        model=Transport 
        fields="__all__"
        
        
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')  
    
class Meta(UserCreationForm.Meta):
    model = User
    fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'email') 
    
    
