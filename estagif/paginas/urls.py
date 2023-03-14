from django.urls import path
from .views import IndexView

urlpatterns = [
    
    path("abc/", IndexView.as_view(), name="pagina-inicial"),

]
