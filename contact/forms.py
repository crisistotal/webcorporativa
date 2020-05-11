# Pasamos a crear el formulario igual que los modelos
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True,label="Nombre", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Escribe tu nombre'}),max_length=100) 
    email = forms.EmailField(required=True,label="E-Mail", widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Escribe tu email'}))
    content = forms.CharField(required=True,label="content",widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Escribe tu mensaje'}),max_length=100)