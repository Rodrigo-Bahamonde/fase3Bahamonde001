from django.shortcuts import render
from .models import ComentarioEndgame,ComentarioDolittle,ComentarioGuerra,ComentarioJoker
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def index(request):

    return render(
        request,
        'index.html',
    )

def galeria(request):

    return render(
        request,
        'galeria.html',
    )

def endgame(request):
    comentario=ComentarioEndgame.objects.all()
    return render(
        request,
        'endgame.html',
        context={'comentario':comentario},
    )

def dolittle(request):
    comentario=ComentarioDolittle.objects.all()
    return render(
        request,
        'dolittle.html',
        context={'comentario':comentario},
    )

def guerra(request):
    comentario=ComentarioGuerra.objects.all()
    return render(
        request,
        'guerra.html',
        context={'comentario': comentario},
    )

def joker(request):
    comentario=ComentarioJoker.objects.all()
    return render(
        request,
        'joker.html',
        context={'comentario':comentario},
    )

class EndgameCreate(CreateView):
    model = ComentarioEndgame
    fields = ['descripcion','comentario','fecha']
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class EndgameUpdate(UpdateView):
    model = ComentarioEndgame
    fields = ['descripcion','comentario']

class EndgameDelete(DeleteView):
    model = ComentarioEndgame
    success_url = reverse_lazy('endgame')



class JokerCreate(CreateView):
    model = ComentarioJoker
    fields = ['descripcion','comentario','fecha']
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class JokerUpdate(UpdateView):
    model = ComentarioJoker
    fields = ['descripcion','comentario']

class JokerDelete(DeleteView):
    model = ComentarioJoker
    success_url = reverse_lazy('joker')



class DolittleCreate(CreateView):
    model = ComentarioDolittle
    fields = ['descripcion','comentario','fecha']
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class DolittleUpdate(UpdateView):
    model = ComentarioDolittle
    fields = ['descripcion','comentario']

class DolittleDelete(DeleteView):
    model = ComentarioDolittle
    success_url = reverse_lazy('dolittle')


class GuerraCreate(CreateView):
    model = ComentarioGuerra
    fields = ['descripcion','comentario','fecha']
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class GuerraUpdate(UpdateView):
    model = ComentarioGuerra
    fields = ['descripcion','comentario']

class GuerraDelete(DeleteView):
    model = ComentarioGuerra
    success_url = reverse_lazy('guerra')





class GuerraListView(generic.ListView):
    model = ComentarioGuerra
    paginate_by = 10
    queryset = ComentarioGuerra.objects.all()

class GuerraDetailView(generic.DetailView):
    model = ComentarioGuerra


class EndgameListView(generic.ListView):
    model = ComentarioEndgame
    paginate_by = 10
    queryset = ComentarioEndgame.objects.all()

class EndgameDetailView(generic.DetailView):
    model = ComentarioEndgame

class JokerListView(generic.ListView):
    model = ComentarioJoker
    paginate_by = 10
    queryset = ComentarioJoker.objects.all()

class JokerDetailView(generic.DetailView):
    model = ComentarioJoker


class DolittleListView(generic.ListView):
    model = ComentarioDolittle
    paginate_by = 10
    queryset = ComentarioDolittle.objects.all()

class DolittleDetailView(generic.DetailView):
    model = ComentarioDolittle