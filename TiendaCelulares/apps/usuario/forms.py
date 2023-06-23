from .models import Celular
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CelularForm(forms.ModelForm):
    class Meta:
        model = Celular
        fields = [
            'marca',
            'precio',
            'descripcion',
            'imagen',
            'disponible',
        ]
        labels = {
            'marca': 'Marca',
            'precio': 'Precio',
            'descripcion': 'Descripcion',
            'imagen': 'Imagen',
             'disponible': 'Disponible',

        }
        widgets = {
            'marca':forms.TextInput(attrs={'class':'form-control'}),
            'precio':forms.TextInput(attrs={'class':'form-control'}),
            'descripcion':forms.TextInput(attrs={'class':'form-control'}),
            'imagen':forms.FileInput(attrs={'class':'form-control','type':'file'}),
             'disponible':forms.TextInput(attrs={'class':'form-control'}),
        }

    
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","first_name", "last_name","email","password1","password2"]
        