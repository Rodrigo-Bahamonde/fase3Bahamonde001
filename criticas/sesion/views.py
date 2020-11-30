from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.contrib.auth.models import User
from .forms import RegistroForm

# Create your views here.

def perfil(request):
    perfil = Perfil.objects.all()
    return render(
        request,
        'perfil.html',
        context={'perfil':perfil},
    )

class RegistroUsuario(CreateView):
    model = User
    form_class = RegistroForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class UsuarioUpdate(UpdateView):
    model = User
    fields = ['first_name','last_name','email']
    success_url = reverse_lazy('perfil')

class UsuarioDelete(DeleteView):
    model = User
    success_url = reverse_lazy('login')


class UsuarioListView(generic.ListView):
    model = User
    paginate_by = 10
    queryset = User.objects.all()

class UsuarioDetail(generic.DetailView):
    model = User
