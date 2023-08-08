from django.urls import path 
from .views import CampusCreate, CampusUpdate, CampusList, CampusDetail, CampusDelete
from .views import CursoCreate, CursoUpdate, CursoList, CursoDetail, CursoDelete
from .views import EstudanteCreate, EstudanteUpdate, EstudanteList, EstudanteDetail, EstudanteDelete
from .views import ServidorCreate, ServidorUpdate, ServidorList, ServidorDetail, ServidorDelete
from .views import UnidadeConcedenteCreate, UnidadeConcedenteUpdate, UnidadeConcedenteList, UnidadeConcedenteDetail, UnidadeConcedenteDelete
from .views import ResponsavelCreate, ResponsavelUpdate, ResponsavelList, ResponsavelDetail, ResponsavelDelete
from .views import IntermediarioCreate, IntermediarioUpdate, IntermediarioList, IntermediarioDetail, IntermediarioDelete
from .views import SituacaoCreate, SituacaoUpdate, SituacaoList, SituacaoDetail, SituacaoDelete
from .views import EstagioCreate, EstagioUpdate, EstagioList, EstagioDetail, EstagioDelete
from .views import RelatorioCreate, RelatorioUpdate, RelatorioList, RelatorioDetail, RelatorioDelete

from .views import EstudanteAutocomplete, OrientadorAutocomplete

from .views import VendaCreate, CarrinhoCreate

urlpatterns = [
    
    path("cadastrar/campus/", CampusCreate.as_view(), name="cadastrar-campus"),
    path("cadastrar/curso/", CursoCreate.as_view(), name="cadastrar-curso"),
    path("cadastrar/estudante/", EstudanteCreate.as_view(), name="cadastrar-estudante"),
    path("cadastrar/servidor/", ServidorCreate.as_view(), name="cadastrar-servidor"),
    path("cadastrar/unidade-concedente/", UnidadeConcedenteCreate.as_view(), name="cadastrar-unidade-concedente"),
    path("cadastrar/responsavel-uc/", ResponsavelCreate.as_view(), name="cadastrar-responsavel"),
    path("cadastrar/intermediario/", IntermediarioCreate.as_view(), name="cadastrar-intermediario"),
    path("cadastrar/situacao-estagio/", SituacaoCreate.as_view(), name="cadastrar-situacao"),
    path("cadastrar/estagio/", EstagioCreate.as_view(), name="cadastrar-estagio"),
    path("cadastrar/relatorio-estagio/", RelatorioCreate.as_view(), name="cadastrar-relatorio"),
    
    path("editar/campus/<int:pk>/", CampusUpdate.as_view(), name="editar-campus"),
    path("editar/curso/<int:pk>/", CursoUpdate.as_view(), name="editar-curso"),
    path("editar/estudante/<int:pk>/", EstudanteUpdate.as_view(), name="editar-estudante"),
    path("editar/servidor/<int:pk>/", ServidorUpdate.as_view(), name="editar-servidor"),
    path("editar/unidade-concedente/<int:pk>/", UnidadeConcedenteUpdate.as_view(), name="editar-unidade-concedente"),
    path("editar/responsavel-uc/<int:pk>/", ResponsavelUpdate.as_view(), name="editar-responsavel"),
    path("editar/intermediario/<int:pk>/", IntermediarioUpdate.as_view(), name="editar-intermediario"),
    path("editar/situacao-estagio/<int:pk>/", SituacaoUpdate.as_view(), name="editar-situacao"),
    path("editar/estagio/<int:pk>/", EstagioUpdate.as_view(), name="editar-estagio"),
    path("editar/relatorio-estagio/<int:pk>/", RelatorioUpdate.as_view(), name="editar-relatorio"),

    path("excluir/campus/<int:pk>/", CampusDelete.as_view(), name="excluir-campus"),
    path("excluir/curso/<int:pk>/", CursoDelete.as_view(), name="excluir-curso"),
    path("excluir/estudante/<int:pk>/", EstudanteDelete.as_view(), name="excluir-estudante"),
    path("excluir/servidor/<int:pk>/", ServidorDelete.as_view(), name="excluir-servidor"),
    path("excluir/unidade-concedente/<int:pk>/", UnidadeConcedenteDelete.as_view(), name="excluir-unidade-concedente"),
    path("excluir/responsavel-uc/<int:pk>/", ResponsavelDelete.as_view(), name="excluir-responsavel"),
    path("excluir/intermediario/<int:pk>/", IntermediarioDelete.as_view(), name="excluir-intermediario"),
    path("excluir/situacao-estagio/<int:pk>/", SituacaoDelete.as_view(), name="excluir-situacao"),
    path("excluir/estagio/<int:pk>/", EstagioDelete.as_view(), name="excluir-estagio"),
    path("excluir/relatorio-estagio/<int:pk>/", RelatorioDelete.as_view(), name="excluir-relatorio"),

    path("listar/campus/", CampusList.as_view(), name="listar-campus"),
    path("listar/curso/", CursoList.as_view(), name="listar-curso"),
    path("listar/estudante/", EstudanteList.as_view(), name="listar-estudante"),
    path("listar/servidor/", ServidorList.as_view(), name="listar-servidor"),
    path("listar/unidade-concedente/", UnidadeConcedenteList.as_view(), name="listar-unidade-concedente"),
    path("listar/responsavel-uc/", ResponsavelList.as_view(), name="listar-responsavel"),
    path("listar/intermediario/", IntermediarioList.as_view(), name="listar-intermediario"),
    path("listar/situacao-estagio/", SituacaoList.as_view(), name="listar-situacao"),
    path("listar/estagio/", EstagioList.as_view(), name="listar-estagio"),
    path("listar/relatorio-estagio/", RelatorioList.as_view(), name="listar-relatorio"),

    path("detalhar/campus/<int:pk>/", CampusDetail.as_view(), name="detalhar-campus"),
    path("detalhar/curso/<int:pk>/", CursoDetail.as_view(), name="detalhar-curso"),
    path("detalhar/estudante/<int:pk>/", EstudanteDetail.as_view(), name="detalhar-estudante"),
    path("detalhar/servidor/<int:pk>/", ServidorDetail.as_view(), name="detalhar-servidor"),
    path("detalhar/unidade-concedente/<int:pk>/", UnidadeConcedenteDetail.as_view(), name="detalhar-unidade-concedente"),
    path("detalhar/responsavel-uc/<int:pk>/", ResponsavelDetail.as_view(), name="detalhar-responsavel"),
    path("detalhar/intermediario/<int:pk>/", IntermediarioDetail.as_view(), name="detalhar-intermediario"),
    path("detalhar/situacao-estagio/<int:pk>/", SituacaoDetail.as_view(), name="detalhar-situacao"),
    path("detalhar/estagio/<int:pk>/", EstagioDetail.as_view(), name="detalhar-estagio"),
    path("detalhar/relatorio-estagio/<int:pk>/", RelatorioDetail.as_view(), name="detalhar-relatorio"),

    # path("editar/campus/<int:pk>/", CampusUpdate.as_view(), name="editar-campus"),
    # path("editar/curso/<int:pk>/", CursoUpdate.as_view(), name="editar-curso"),


    path("vender/", VendaCreate.as_view(), name="vender"),
    path("adicionar/", CarrinhoCreate.as_view(), name="adicionar"),

    # URL do autocomplete
    path("buscar/estudante/", EstudanteAutocomplete.as_view(), name="buscar-estudante"),
    path("buscar/orientador/", OrientadorAutocomplete.as_view(), name="buscar-orientador"),

]
