from django.contrib import admin
from .models import Campus, Curso, Estudante, Servidor, UnidadeConcedente
from .models import Responsavel, Intermediario, Situacao, Estagio, Historico, Relatorio

# Register your models here.
admin.site.register(Campus)
admin.site.register(Curso)
admin.site.register(Estudante)
admin.site.register(Servidor)
admin.site.register(UnidadeConcedente)
admin.site.register(Responsavel)
admin.site.register(Intermediario)
admin.site.register(Situacao)
admin.site.register(Estagio)
admin.site.register(Historico)
admin.site.register(Relatorio)


from .models import Produto, Venda, ProdutoVenda, Carinho
admin.site.register(Produto)
admin.site.register(Venda)
admin.site.register(ProdutoVenda)
admin.site.register(Carinho)

