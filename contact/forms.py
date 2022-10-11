import email
from tkinter import Widget
from unicodedata import name
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Ingresa tu nombre"}))
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': "Ingresa tu email"}))
    # en formularios no se usa el textfield, solo charfield
    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 5, 'placeholder': "Ingresa tu mensaje"}))
