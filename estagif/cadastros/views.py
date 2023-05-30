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

from django.shortcuts import get_object_or_404

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


class CursoCreate(LoginRequiredMixin, CreateView):
    model = Curso
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-curso")
    extra_context = {"titulo": "Cadastro de Curso"}


class EstudanteCreate(LoginRequiredMixin, CreateView):
    model = Estudante
    fields = [
        "nome", "cpf", "data_nascimento", "telefone", "email",
        "matricula", "curso", "campus",
    ]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-estudante")
    extra_context = {"titulo": "Cadastro de Estudante"}


class ServidorCreate(LoginRequiredMixin, CreateView):
    model = Servidor
    fields = [
        "nome","cpf","data_nascimento","telefone",
        "email","siape","campus",
    ]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-servidor")


class UnidadeConcedenteCreate(LoginRequiredMixin, CreateView):
    model = UnidadeConcedente
    fields = ["nome", "documento", "telefone", "email",]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-unidade-concedente")


class ResponsavelCreate(LoginRequiredMixin, CreateView):
    model = Responsavel
    fields = ["nome", "email", "telefone", "cpf", "empresa",]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-responsavel")


class IntermediarioCreate(LoginRequiredMixin, CreateView):
    model = Intermediario
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-intermediario")


class SituacaoCreate(LoginRequiredMixin, CreateView):
    model = Situacao
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-situacao")


class EstagioCreate(LoginRequiredMixin, CreateView):
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


class RelatorioCreate(LoginRequiredMixin, CreateView):
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


class CampusUpdate(LoginRequiredMixin, UpdateView):
    model = Campus
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-campus")


class CursoUpdate(LoginRequiredMixin, UpdateView):
    model = Curso
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-curso")


class EstudanteUpdate(LoginRequiredMixin, UpdateView):
    model = Estudante
    fields = [
        "nome", "cpf", "data_nascimento", "telefone", "email",
        "matricula", "curso", "campus",
    ]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-estudante")


class ServidorUpdate(LoginRequiredMixin, UpdateView):
    model = Servidor
    fields = [
        "nome","cpf","data_nascimento","telefone",
        "email","siape","campus",
    ]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-servidor")


class UnidadeConcedenteUpdate(LoginRequiredMixin, UpdateView):
    model = UnidadeConcedente
    fields = ["nome", "documento", "telefone", "email",]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-unidade-concedente")


class ResponsavelUpdate(LoginRequiredMixin, UpdateView):
    model = Responsavel
    fields = ["nome", "email", "telefone", "cpf", "empresa",]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-responsavel")


class IntermediarioUpdate(LoginRequiredMixin, UpdateView):
    model = Intermediario
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-intermediario")


class SituacaoUpdate(LoginRequiredMixin, UpdateView):
    model = Situacao
    fields = ["nome"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-situacao")


class EstagioUpdate(LoginRequiredMixin, UpdateView):
    model = Estagio
    fields = [
        "estudante", "intermediario", "unidade_concedente", "responssvel_empresa",
        "orientador", "data_inicio", "data_termino", "ch_semanal",
        "situacao", "observacoes",
    ]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-estagio")

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


class RelatorioUpdate(LoginRequiredMixin, UpdateView):
    model = Relatorio
    fields = [
        "estagio", "data_inicio", "data_termino",
        "tipo", "entregue", "data_cadastro",
    ]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar-relatorio")

##################################################


class CampusDelete(LoginRequiredMixin, DeleteView):
    model = Campus
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-campus")


class CursoDelete(LoginRequiredMixin, DeleteView):  
    model = Curso
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-curso")


class EstudanteDelete(LoginRequiredMixin, DeleteView):
    model = Estudante
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-estudante")


class ServidorDelete(LoginRequiredMixin, DeleteView):
    model = Servidor
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-servidor")


class UnidadeConcedenteDelete(LoginRequiredMixin, DeleteView):
    model = UnidadeConcedente
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-unidade-concedente")


class ResponsavelDelete(LoginRequiredMixin, DeleteView):
    model = Responsavel
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-responsavel")


class IntermediarioDelete(LoginRequiredMixin, DeleteView):
    model = Intermediario
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-intermediario")


class SituacaoDelete(LoginRequiredMixin, DeleteView):
    model = Situacao
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-situacao")


class EstagioDelete(LoginRequiredMixin, DeleteView):
    model = Estagio
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-estagio")

    # def get_object(self):
    #     self.object = get_object_or_404(
    #             Estagio, 
    #             pk=self.kwargs["pk"],
    #             cadastrado_por=self.request.user
    #         )

    #     return self.object


class RelatorioDelete(LoginRequiredMixin, DeleteView):
    model = Relatorio
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy("listar-relatorio")


##################################################


class CampusList(LoginRequiredMixin, ListView):
    model = Campus
    template_name = "cadastros/list/campus.html"


class CursoList(LoginRequiredMixin, ListView):
    model = Curso
    template_name = "cadastros/list/curso.html"


class EstudanteList(LoginRequiredMixin, ListView):  
    model = Estudante
    template_name = "cadastros/list/estudante.html"


class ServidorList(LoginRequiredMixin, ListView):
    model = Servidor
    template_name = "cadastros/list/servidor.html"


class UnidadeConcedenteList(LoginRequiredMixin, ListView):
    model = UnidadeConcedente
    template_name = "cadastros/list/unidade-concedente.html"


class ResponsavelList(LoginRequiredMixin, ListView):
    model = Responsavel
    template_name = "cadastros/list/responsavel.html"


class IntermediarioList(LoginRequiredMixin, ListView):
    model = Intermediario
    template_name = "cadastros/list/intermediario.html"


class SituacaoList(LoginRequiredMixin, ListView):
    model = Situacao
    template_name = "cadastros/list/situacao.html"


class EstagioList(LoginRequiredMixin, ListView):
    model = Estagio
    template_name = "cadastros/list/estagio.html"

    # # Altera a consulta padrão de um ListView que é listar todos os registros
    # def get_queryset(self):
    #     # o object_list é utilizado lá no for do HTML para armazenar uma lista de objetos
    #     # Precisamos retornar essa lista
    #     return Estagio.objects.filter(cadastrado_por=self.request.user)


class RelatorioList(LoginRequiredMixin, ListView):
    model = Relatorio
    template_name = "cadastros/list/relatorio.html"


##################################################


class CampusDetail(LoginRequiredMixin, DetailView):
    model = Campus
    template_name = "cadastros/detail/campus.html"


class CursoDetail(LoginRequiredMixin, DetailView):
    model = Curso
    template_name = "cadastros/detail/curso.html"


class EstudanteDetail(LoginRequiredMixin, DetailView):
    model = Estudante
    template_name = "cadastros/detail/estudante.html"


class ServidorDetail(LoginRequiredMixin, DetailView):
    model = Servidor
    template_name = "cadastros/detail/servidor.html"


class UnidadeConcedenteDetail(LoginRequiredMixin, DetailView):
    model = UnidadeConcedente
    template_name = "cadastros/detail/unidade-concedente.html"


class ResponsavelDetail(LoginRequiredMixin, DetailView):
    model = Responsavel
    template_name = "cadastros/detail/responsavel.html"


class IntermediarioDetail(LoginRequiredMixin, DetailView):
    model = Intermediario
    template_name = "cadastros/detail/intermediario.html"


class SituacaoDetail(LoginRequiredMixin, DetailView):
    model = Situacao
    template_name = "cadastros/detail/situacao.html"


class EstagioDetail(LoginRequiredMixin, DetailView):
    model = Estagio
    template_name = "cadastros/detail/estagio.html"


class RelatorioDetail(LoginRequiredMixin, DetailView):
    model = Relatorio
    template_name = "cadastros/detail/relatorio.html"


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
        prod_carrinho = Carinho.objects.all()

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
        
