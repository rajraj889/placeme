from django import forms
from .models import company,Post,study  
from django.forms import ModelForm, Textarea
class company_added(forms.ModelForm):
    class Meta():
        model= company
        fields= ["name", "visit_date", "no_recruited"]
        #fields='__all__'

class exp_added(forms.ModelForm):
    class Meta():
        model= Post
        fields= ["name", "company",'email', "content"]  

class study_exp(forms.ModelForm):
    class Meta():
        model= study
        fields= ["name", "college",'email', "content"]
