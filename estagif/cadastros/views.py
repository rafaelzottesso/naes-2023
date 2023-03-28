from .models import Campus, Curso, UnidadeConcedente, Responsavel

from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.


class CampusCreate(CreateView):
    model = Campus
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("pagina-inicial")


class CursoCreate(CreateView):
    model = Curso
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("pagina-inicial")


##################################################


class CampusUpdate(UpdateView):
    model = Campus
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("pagina-inicial")


class CursoUpdate(UpdateView):
    model = Curso
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("pagina-inicial")
