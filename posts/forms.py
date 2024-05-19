from django import forms
from .models import Poste , Stage 
from student.models import Logement , Transport ,Recommandation , Evénement ,EvenClub ,EvenSocial

class PostForm(forms.ModelForm):
    class Meta:
        model = Poste
        fields = "__all__" 
        
class StageForm(forms.ModelForm):
    class Meta:
        model = Stage
        fields = "__all__" 
 

class LogementForm(forms.ModelForm):
    class Meta:
        model = Logement
        fields = "__all__" 
        
class TransportForm(forms.ModelForm):
    class Meta:
        model = Transport
        fields = "__all__"  
        
class RecommandationForm(forms.ModelForm):
    class Meta:
        model = Recommandation
        fields = "__all__"  
        

class EvenClubForm(forms.ModelForm):
    class Meta:
        model = EvenClub
        fields = "__all__"
        
        
class EvenSocialForm(forms.ModelForm):
    class Meta:
        model = EvenSocial
        fields = "__all__" 


