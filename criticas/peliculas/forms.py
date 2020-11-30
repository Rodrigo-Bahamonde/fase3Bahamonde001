from django.shortcuts import render
from . models import ComentarioDolittle
from django.views import generic
from django import forms



class ComentarioForm(forms.Form):
    descripcion = forms.CharField(max_length= 50)
    comentario = forms.CharField(max_length=200)
    fecha = forms.DateField()
    usuario = forms.CharField(max_length=50)