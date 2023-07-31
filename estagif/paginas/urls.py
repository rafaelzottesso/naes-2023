from django.urls import path
from .views import IndexView, CriarSessaoView, DeletarSessaoView

urlpatterns = [
    
    path("", IndexView.as_view(), name="pagina-inicial"),
    path("ativar/fazenda/<int:pk>/", CriarSessaoView.as_view(), name="criar-sessao"),
    path("desativar/fazenda/", DeletarSessaoView.as_view(), name="deletar-sessao"),

]
