from django.urls import path
from .views import CampusCreate, CampusUpdate
from .views import CursoCreate, CursoUpdate

urlpatterns = [
    
    path("cadastrar/campus/", CampusCreate.as_view(), name="cadastrar-campus"),
    path("cadastrar/curso/", CursoCreate.as_view(), name="cadastrar-curso"),

    path("editar/campus/<int:pk>/", CampusUpdate.as_view(), name="editar-campus"),
    path("editar/curso/<int:pk>/", CursoUpdate.as_view(), name="editar-curso"),


]
