from typing import Any, Optional
from django.db import models
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from .models import Campus, Curso, UnidadeConcedente, Responsavel
from .models import Estudante, Servidor, Intermediario, Situacao, Estagio, Relatorio
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from django.shortcuts import get_object_or_404

# Framework de mensagens/notificações
from django.contrib.messages.views import SuccessMessageMixin

# Importação da biblioteca do autocomplete
from dal import autocomplete

# Importação dos meus formulários personalizados
from .forms import EstagioForm

# Create your views here.


class CampusCreate(GroupRequiredMixin, SuccessMessageMixin, CreateView):
    model = Campus
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-campus")
    group_required = ["Administrador"]
    success_message = "Campus %(nome)s inserido com sucesso!"

    def get_context_data(self, *args, **kwargs):

        dados = super().get_context_data(*args, **kwargs)
        dados["titulo"] = "Cadastro de Campus"
        return dados


class CursoCreate(GroupRequiredMixin, SuccessMessageMixin, CreateView):
    model = Curso
    fields = ["nome", "campus"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-curso")
    extra_context = {"titulo": "Cadastro de Curso"}
    group_required = ["Administrador"]
    success_message = "Curso %(nome)s inserido com sucesso!"


class EstudanteCreate(GroupRequiredMixin, SuccessMessageMixin, CreateView):
    model = Estudante
    fields = [
        "nome", "cpf", "data_nascimento", "telefone", "email",
        "matricula", "curso", "campus",
    ]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-estudante")
    extra_context = {"titulo": "Cadastro de Estudante"}
    group_required = ["Administrador"]
    success_message = "Estudante %(nome)s inserido com sucesso!"


class ServidorCreate(GroupRequiredMixin, SuccessMessageMixin, CreateView):
    model = Servidor
    fields = [
        "nome","cpf","data_nascimento","telefone",
        "email","siape","campus",
    ]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-servidor")
    group_required = ["Administrador"]
    success_message = "Servidor %(nome)s inserido com sucesso!"


class UnidadeConcedenteCreate(GroupRequiredMixin, SuccessMessageMixin, CreateView):
    model = UnidadeConcedente
    fields = ["nome", "documento", "telefone", "email",
              "cep", "logradouro", "numero", "bairro", "cidade"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-unidade-concedente")
    group_required = ["Administrador"]
    success_message = "Unidade Concedente %(nome)s inserida com sucesso!"


class ResponsavelCreate(GroupRequiredMixin, SuccessMessageMixin, CreateView):
    model = Responsavel
    fields = ["nome", "email", "telefone", "cpf", "empresa",]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-responsavel")
    group_required = ["Administrador"]
    success_message = "Responsável %(nome)s inserido com sucesso!"


class IntermediarioCreate(GroupRequiredMixin, SuccessMessageMixin, CreateView):
    model = Intermediario
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-intermediario")
    group_required = ["Administrador"]
    success_message = "Intermediário %(nome)s inserido com sucesso!"


class SituacaoCreate(GroupRequiredMixin, SuccessMessageMixin, CreateView):
    model = Situacao
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-situacao")
    group_required = ["Administrador"]
    success_message = "Situação %(nome)s inserida com sucesso!"


class EstagioCreate(GroupRequiredMixin, SuccessMessageMixin, CreateView):
    # Usar o form que a gente criou para criar o campo autocomplete
    # Para isso, tiramos o "model" e o "fields" daqui e colocamos no forms.py
    # Assim, precisamos criar o atributo "form_class"
    form_class = EstagioForm
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-estagio")
    group_required = ["Administrador"]
    success_message = "Estágio inserido com sucesso!"

    # Método padrão chamado quando um formulário é submetido
    def form_valid(self, form): 
        # Neste ponto, ainda não temos um objeto, apenas os dados do formulário por meio do "form.instance.atributo"
        form.instance.cadastrado_por = self.request.user
        
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
        
        if(form.instance.estudante == form.instance.orientador):
            form.add_error("estudante", "Você não pode ser seu próprio orientador!")
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


class RelatorioCreate(GroupRequiredMixin, SuccessMessageMixin, CreateView):
    model = Relatorio
    fields = [
        "estagio", "data_inicio", "data_termino",
        "tipo", "entregue", "data_cadastro",
    ]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-relatorio")
    group_required = ["Administrador"]
    success_message = "Relatório inserido com sucesso!"

    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        return super().form_valid(form)


##################################################


class CampusUpdate(GroupRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Campus
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-campus")
    group_required = ["Administrador"]
    success_message = "Campus %(nome)s atualizado com sucesso!"


class CursoUpdate(GroupRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Curso
    fields = ["nome", "campus"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-curso")
    group_required = ["Administrador"]
    success_message = "Curso %(nome)s atualizado com sucesso!"


class EstudanteUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Estudante
    fields = [
        "nome", "cpf", "data_nascimento", "telefone", "email",
        "matricula", "curso", "campus",
    ]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-estudante")
    success_message = "Estudante %(nome)s atualizado com sucesso!"


class ServidorUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Servidor
    fields = [
        "nome","cpf","data_nascimento","telefone",
        "email","siape","campus",
    ]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-servidor")
    success_message = "Servidor %(nome)s atualizado com sucesso!"


class UnidadeConcedenteUpdate(GroupRequiredMixin, SuccessMessageMixin, UpdateView):
    model = UnidadeConcedente
    fields = ["nome", "documento", "telefone", "email",
              "cep", "logradouro", "numero", "bairro", "cidade"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-unidade-concedente")
    group_required = ["Administrador"]
    success_message = "Unidade Concedente %(nome)s inserida com sucesso!"


class ResponsavelUpdate(GroupRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Responsavel
    fields = ["nome", "email", "telefone", "cpf", "empresa",]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-responsavel")
    group_required = ["Administrador"]
    success_message = "Responsável %(nome)s atualizado com sucesso!"


class IntermediarioUpdate(GroupRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Intermediario
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-intermediario")
    group_required = ["Administrador"]
    success_message = "Intermediário %(nome)s atualizado com sucesso!"


class SituacaoUpdate(GroupRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Situacao
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-situacao")
    group_required = ["Administrador"]
    success_message = "Situação %(nome)s inserida com sucesso!"


class EstagioUpdate(GroupRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Estagio
    fields = [
        "estudante", "intermediario", "unidade_concedente", "responssvel_empresa",
        "orientador", "data_inicio", "data_termino", "ch_semanal",
        "situacao", "observacoes",
    ]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-estagio")
    group_required = ["Administrador"]
    success_message = "Estágio atualizado com sucesso!"

    # def get_object(self):
    #     self.object = get_object_or_404(
    #             Estagio, 
    #             pk=self.kwargs["pk"],
    #             cadastrado_por=self.request.user
    #         )

    #     # o get traz um objeto e o filter um array de objetos
    #     # self.object = Estagio.objects.get(
    #     #         pk=self.kwargs["pk"],
    #     #         cadastrado_por=self.request.user
    #     #     )
    #     return self.object


class RelatorioUpdate(GroupRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Relatorio
    fields = [
        "estagio", "data_inicio", "data_termino",
        "tipo", "entregue", "data_cadastro",
    ]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-relatorio")
    group_required = ["Administrador"]
    success_message = "Relatório atualizado com sucesso!"

##################################################


class CampusDelete(GroupRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Campus
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-campus")
    group_required = ["Administrador"]
    success_message = "Campus excluído com sucesso!"


class CursoDelete(GroupRequiredMixin, SuccessMessageMixin, DeleteView):  
    model = Curso
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-curso")
    group_required = ["Administrador"]
    success_message = "Curso excluído com sucesso!"


class EstudanteDelete(GroupRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Estudante
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-estudante")
    group_required = ["Administrador"]
    success_message = "Estudante excluído com sucesso!"


class ServidorDelete(GroupRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Servidor
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-servidor")
    group_required = ["Administrador"]
    success_message = "Servidor excluído com sucesso!"


class UnidadeConcedenteDelete(GroupRequiredMixin, SuccessMessageMixin, DeleteView):
    model = UnidadeConcedente
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-unidade-concedente")
    group_required = ["Administrador"]
    success_message = "Unidade Concedente excluída com sucesso!"


class ResponsavelDelete(GroupRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Responsavel
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-responsavel")
    group_required = ["Administrador"]
    success_message = "Responsavél excluído com sucesso!"


class IntermediarioDelete(GroupRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Intermediario
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-intermediario")
    group_required = ["Administrador"]
    success_message = "Intermediário excluído com sucesso!"


class SituacaoDelete(GroupRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Situacao
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-situacao")
    group_required = ["Administrador"]
    success_message = "Situação excluída com sucesso!"


class EstagioDelete(GroupRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Estagio
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-estagio")
    group_required = ["Administrador"]
    success_message = "Estágio excluído com sucesso!"

    # def get_object(self):
    #     self.object = get_object_or_404(
    #             Estagio, 
    #             pk=self.kwargs["pk"],
    #             cadastrado_por=self.request.user
    #         )

    #     return self.object


class RelatorioDelete(GroupRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Relatorio
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-relatorio")
    group_required = ["Administrador"]
    success_message = "Relatório excluído com sucesso!"


##################################################


class CampusList(GroupRequiredMixin, ListView):
    model = Campus
    template_name = "cadastros/list/campus.html"
    group_required = ["Administrador"]
    paginate_by = 50


class CursoList(GroupRequiredMixin, ListView):
    model = Curso
    template_name = "cadastros/list/curso.html"
    group_required = ["Administrador"]
    paginate_by = 50

    def get_queryset(self):
        self.object_list = Curso.objects.all().select_related("campus")
        return self.object_list


class EstudanteList(GroupRequiredMixin, ListView):  
    model = Estudante
    template_name = "cadastros/list/estudante.html"
    group_required = ["Administrador"]
    paginate_by = 50


class ServidorList(GroupRequiredMixin, ListView):
    model = Servidor
    template_name = "cadastros/list/servidor.html"
    group_required = ["Administrador"]
    paginate_by = 50


class UnidadeConcedenteList(GroupRequiredMixin, ListView):
    model = UnidadeConcedente
    template_name = "cadastros/list/unidade-concedente.html"
    group_required = ["Administrador"]
    paginate_by = 50


class ResponsavelList(GroupRequiredMixin, ListView):
    model = Responsavel
    template_name = "cadastros/list/responsavel.html"
    group_required = ["Administrador"]
    paginate_by = 50

    def get_queryset(self):
        self.object_list = Responsavel.objects.all().select_related("empresa")
        return self.object_list


class IntermediarioList(GroupRequiredMixin, ListView):
    model = Intermediario
    template_name = "cadastros/list/intermediario.html"
    group_required = ["Administrador"]
    paginate_by = 50


class SituacaoList(GroupRequiredMixin, ListView):
    model = Situacao
    template_name = "cadastros/list/situacao.html"
    group_required = ["Administrador"]
    paginate_by = 50


class EstagioList(GroupRequiredMixin, ListView):
    model = Estagio
    template_name = "cadastros/list/estagio.html"
    group_required = ["Administrador"]
    paginate_by = 50

    # Altera a consulta padrão de um ListView que é listar todos os registros
    def get_queryset(self):
        # o object_list é utilizado lá no for do HTML para armazenar uma lista de objetos
        # Precisamos retornar essa lista
        return Estagio.objects.all().select_related(
            "estudante",
            "intermediario",
            "unidade_concedente",
            "responssvel_empresa",
            "orientador",
            "situacao",
        )


class RelatorioList(GroupRequiredMixin, ListView):
    model = Relatorio
    template_name = "cadastros/list/relatorio.html"
    group_required = ["Administrador"]
    paginate_by = 50


##################################################


class CampusDetail(GroupRequiredMixin, DetailView):
    model = Campus
    template_name = "cadastros/detail/campus.html"
    group_required = ["Administrador"]


class CursoDetail(GroupRequiredMixin, DetailView):
    model = Curso
    template_name = "cadastros/detail/curso.html"
    group_required = ["Administrador"]


class EstudanteDetail(GroupRequiredMixin, DetailView):
    model = Estudante
    template_name = "cadastros/detail/estudante.html"
    group_required = ["Administrador"]


class ServidorDetail(GroupRequiredMixin, DetailView):
    model = Servidor
    template_name = "cadastros/detail/servidor.html"
    group_required = ["Administrador"]


class UnidadeConcedenteDetail(GroupRequiredMixin, DetailView):
    model = UnidadeConcedente
    template_name = "cadastros/detail/unidade-concedente.html"
    group_required = ["Administrador"]


class ResponsavelDetail(GroupRequiredMixin, DetailView):
    model = Responsavel
    template_name = "cadastros/detail/responsavel.html"
    group_required = ["Administrador"]


class IntermediarioDetail(GroupRequiredMixin, DetailView):
    model = Intermediario
    template_name = "cadastros/detail/intermediario.html"
    group_required = ["Administrador"]


class SituacaoDetail(GroupRequiredMixin, DetailView):
    model = Situacao
    template_name = "cadastros/detail/situacao.html"
    group_required = ["Administrador"]


class EstagioDetail(GroupRequiredMixin, DetailView):
    model = Estagio
    template_name = "cadastros/detail/estagio.html"
    group_required = ["Administrador"]


class RelatorioDetail(GroupRequiredMixin, DetailView):
    model = Relatorio
    template_name = "cadastros/detail/relatorio.html"
    group_required = ["Administrador"]


##################################################


# Exemplo da venda
from .models import Produto, Venda, ProdutoVenda, Carinho

class CarrinhoCreate(CreateView):
    model = Carinho
    template_name = "cadastros/form.html"
    fields = ["produto", "quantidade"]
    success_url = reverse_lazy("pagina-inicial")

class VendaCreate(CreateView):
    model = Venda
    template_name = "cadastros/form.html"
    fields = ["cliente", "forma_pagamento"]
    success_url = reverse_lazy("pagina-inicial")

    # Na hora que for salvar a venda...
    def form_valid(self, form):
        # Define um valor porque é obrigatório
        form.instance.valor_total = 0.0
        
        # Cria a venda no banco e o object
        url = super().form_valid(form)

        # Busca todos os produtos que estão no carrinho
        prod_carrinho = Carinho.objects.filter(usuario=self.request.user)

        if(prod_carrinho.count() == 0):
            form.add_error("", "Nenhum item adicionado para finalizar a Venda.")
            return super().form_invalid(form)

        valor_total = 0.0

        # Para cada produto registrado no carrinho...
        for c in prod_carrinho:

            valor_total += (float(c.produto.valor) * c.quantidade)

            ProdutoVenda.objects.create(
                venda = self.object,
                produto = c.produto,
                quantidade = c.quantidade,
                valor=c.produto.valor * c.quantidade
            )

            c.delete()

        # Atualiza o objedo da venda com o valor total novo
        self.object.valor_total = valor_total
        # Faz o UPDATE no banco de dados
        self.object.save()


        return url
        
############## AUTOCOMPLETE ################

# Criar uma view com essa herança e que retorne uma lista de objetos
class EstudanteAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        object_list = Estudante.objects.all()

        # Pega o termo do campo e faz um filtro nele
        if self.q:
            object_list = object_list.filter(
                nome__icontains=self.q
            )
        # Retorna a lista de objetos
        return object_list


class OrientadorAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        object_list = Servidor.objects.all()

        # Pega o termo do campo e faz um filtro nele
        if self.q:
            object_list = object_list.filter(
                nome__icontains=self.q
            )
        # Retorna a lista de objetos
        return object_list