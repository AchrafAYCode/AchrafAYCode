from django.forms import ModelForm 
from .models import Poste  , Recommandation ,Transport ,Logement ,Stage ,Evénement ,EvenClub ,EvenSocial 
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
        

        
class StageForm(ModelForm): 
    class Meta : 
        model=Stage 
        fields="__all__" 
        
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')  
    
class Meta(UserCreationForm.Meta):
    model = User
    fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'email') 
    
    


from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Logement

class LogementForm(forms.ModelForm):
   
    def __init__(self, *args, **kwargs):
        super(LogementForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Enregistrer'))

    class Meta:
        model = Logement
        fields = ['localisation', 'description', 'contactinfo']