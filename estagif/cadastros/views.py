from .models import Campus, Curso, UnidadeConcedente, Responsavel
from .models import Estudante, Servidor, Intermediario, Situacao, Estagio, Relatorio
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.


class CampusCreate(CreateView):
    model = Campus
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-campus")

    def get_context_data(self, *args, **kwargs):

        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Cadastro de Campus"
        return dados


class CursoCreate(CreateView):
    model = Curso
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-curso")


class EstudanteCreate(CreateView):
    model = Estudante
    fields = [
        "nome", "cpf", "data_nascimento", "telefone", "email",
        "matricula", "curso", "campus",
    ]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-estudante")


class ServidorCreate(CreateView):
    model = Servidor
    fields = [
        "nome","cpf","data_nascimento","telefone",
        "email","siape","campus",
    ]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-servidor")


class UnidadeConcedenteCreate(CreateView):
    model = UnidadeConcedente
    fields = ["nome", "documento", "telefone", "email",]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-unidade-concedente")


class ResponsavelCreate(CreateView):
    model = Responsavel
    fields = ["nome", "email", "telefone", "cpf", "empresa",]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-responsavel")


class IntermediarioCreate(CreateView):
    model = Intermediario
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-intermediario")


class SituacaoCreate(CreateView):
    model = Situacao
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-situacao")


class EstagioCreate(CreateView):
    model = Estagio
    fields = [
        "estudante", "intermediario", "unidade_concedente", "responssvel_empresa",
        "orientador", "data_inicio", "data_termino", "ch_semanal",
        "situacao", "observacoes",
    ]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-estagio")


class RelatorioCreate(CreateView):
    model = Relatorio
    fields = [
        "estagio", "data_inicio", "data_termino",
        "tipo", "entregue", "data_cadastro",
    ]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-relatorio")


##################################################


class CampusUpdate(UpdateView):
    model = Campus
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-campus")


class CursoUpdate(UpdateView):
    model = Curso
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-curso")


class EstudanteUpdate(UpdateView):
    model = Estudante
    fields = [
        "nome", "cpf", "data_nascimento", "telefone", "email",
        "matricula", "curso", "campus",
    ]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-estudante")


class ServidorUpdate(UpdateView):
    model = Servidor
    fields = [
        "nome","cpf","data_nascimento","telefone",
        "email","siape","campus",
    ]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-servidor")


class UnidadeConcedenteUpdate(UpdateView):
    model = UnidadeConcedente
    fields = ["nome", "documento", "telefone", "email",]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-unidade-concedente")


class ResponsavelUpdate(UpdateView):
    model = Responsavel
    fields = ["nome", "email", "telefone", "cpf", "empresa",]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-responsavel")


class IntermediarioUpdate(UpdateView):
    model = Intermediario
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-intermediario")


class SituacaoUpdate(UpdateView):
    model = Situacao
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-situacao")


class EstagioUpdate(UpdateView):
    model = Estagio
    fields = [
        "estudante", "intermediario", "unidade_concedente", "responssvel_empresa",
        "orientador", "data_inicio", "data_termino", "ch_semanal",
        "situacao", "observacoes",
    ]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-estagio")


class RelatorioUpdate(UpdateView):
    model = Relatorio
    fields = [
        "estagio", "data_inicio", "data_termino",
        "tipo", "entregue", "data_cadastro",
    ]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-relatorio")


##################################################

class CampusDelete(DeleteView):
    model = Campus
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-campus")


class CursoDelete(DeleteView):  
    model = Curso
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-curso")


class EstudanteDelete(DeleteView):
    model = Estudante
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-estudante")


class ServidorDelete(DeleteView):
    model = Servidor
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-servidor")


class UnidadeConcedenteDelete(DeleteView):
    model = UnidadeConcedente
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-unidade-concedente")


class ResponsavelDelete(DeleteView):
    model = Responsavel
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-responsavel")


class IntermediarioDelete(DeleteView):
    model = Intermediario
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-intermediario")


class SituacaoDelete(DeleteView):
    model = Situacao
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-situacao")


class EstagioDelete(DeleteView):
    model = Estagio
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-estagio")


class RelatorioDelete(DeleteView):
    model = Relatorio
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-relatorio")


##################################################


class CampusList(ListView):
    model = Campus
    template_name = "cadastros/list/campus.html"


class CursoList(ListView):
    model = Curso
    template_name = "cadastros/list/curso.html"


class EstudanteList(ListView):  
    model = Estudante
    template_name = "cadastros/list/estudante.html"


class ServidorList(ListView):
    model = Servidor
    template_name = "cadastros/list/servidor.html"


class UnidadeConcedenteList(ListView):
    model = UnidadeConcedente
    template_name = "cadastros/list/unidade-concedente.html"


class ResponsavelList(ListView):
    model = Responsavel
    template_name = "cadastros/list/responsavel.html"


class IntermediarioList(ListView):
    model = Intermediario
    template_name = "cadastros/list/intermediario.html"


class SituacaoList(ListView):
    model = Situacao
    template_name = "cadastros/list/situacao.html"


class EstagioList(ListView):
    model = Estagio
    template_name = "cadastros/list/estagio.html"


class RelatorioList(ListView):
    model = Relatorio
    template_name = "cadastros/list/relatorio.html"


##################################################


class CampusDetail(DetailView):
    model = Campus
    template_name = "cadastros/detail/campus.html"


class CursoDetail(DetailView):
    model = Curso
    template_name = "cadastros/detail/curso.html"


class EstudanteDetail(DetailView):
    model = Estudante
    template_name = "cadastros/detail/estudante.html"


class ServidorDetail(DetailView):
    model = Servidor
    template_name = "cadastros/detail/servidor.html"


class UnidadeConcedenteDetail(DetailView):
    model = UnidadeConcedente
    template_name = "cadastros/detail/unidade-concedente.html"


class ResponsavelDetail(DetailView):
    model = Responsavel
    template_name = "cadastros/detail/responsavel.html"


class IntermediarioDetail(DetailView):
    model = Intermediario
    template_name = "cadastros/detail/intermediario.html"


class SituacaoDetail(DetailView):
    model = Situacao
    template_name = "cadastros/detail/situacao.html"


class EstagioDetail(DetailView):
    model = Estagio
    template_name = "cadastros/detail/estagio.html"


class RelatorioDetail(DetailView):
    model = Relatorio
    template_name = "cadastros/detail/relatorio.html"


##################################################

