from .models import Campus, Curso, UnidadeConcedente, Responsavel
from .models import Estudante, Servidor, Intermediario, Situacao, Estagio, Relatorio
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class CampusCreate(LoginRequiredMixin, CreateView):
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
    extra_context = {"titulo": "Cadastro de Curso"}


class EstudanteCreate(CreateView):
    model = Estudante
    fields = [
        "nome", "cpf", "data_nascimento", "telefone", "email",
        "matricula", "curso", "campus",
    ]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-estudante")
    extra_context = {"titulo": "Cadastro de Estudante"}


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

    # Método padrão chamado quando um formulário é submetido
    def form_valid(self, form):
        # Neste ponto, ainda não temos um objeto, apenas os dados do formulário por meio do "form.instance.atributo"
        form.instance.usuario = self.request.user
        
        # Aqui é póssivel fazer qualquer coisa com os dados do formulário, antes de fazer o INSERT no banco ou aquelas
        # validações que não são possíveis fazer no models.py

        # No exemplo a seguir, estamos verificando se a data de início é igual ou posterior a data de término
        if(form.instance.data_inicio >= form.instance.data_termino):
            # Se isso for verdade, temos que adicionar um erro no formulário
            # O erro é adicionado no campo data_inicio com a mensagem abaixo
            form.add_error("data_inicio", "A data de início deve ser menor que a data de término")
            # Também podemos adicionar um erro no data_termino, porém sem mensagem pra não ficar repetitivo
            form.add_error("data_termino", "")
            # Por fim, retornamos o usuário de volta para o formulário com os erros
            return super().form_invalid(form)

        # Aqui cria-se o objeto e salva o registro no banco de dados.
        # O super() faz todas as validações que encontrar no models.py
        # O comportamento padrão é redirecionar para a URL de sucesso caso todas as validações sejam atendidas
        url = super().form_valid(form)

        # Podemos acessar o objeto criado e modificar alguma coisa
        # self.object.atributo = "valor"
        # porém, precisamos salvar esse objeto para que o Django faça o UPDATE no banco de dados
        # self.object.save()

        # Por fim, retornamos a URL de sucesso do success_url
        return url


class RelatorioCreate(CreateView):
    model = Relatorio
    fields = [
        "estagio", "data_inicio", "data_termino",
        "tipo", "entregue", "data_cadastro",
    ]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-relatorio")

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        return super().form_valid(form)


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

