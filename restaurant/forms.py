from django import forms
from .models import Menu, Plats

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nom du menu'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description du menu'}),
        }
        
class PlatsForm(forms.ModelForm):
    class Meta:
        model = Plats
        fields = ['menu','name', 'description', 'price', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nom du plat'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description du plat'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Prix du plat'}),
        }