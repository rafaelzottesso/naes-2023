from cadastros.models import Estagio, Estudante, Servidor
from django.views.generic import TemplateView
import datetime


class IndexView(TemplateView):
    template_name = "paginas/index.html"
    
    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)

        if (self.request.user.is_authenticated):

            dados["estagios_estudante"] = Estagio.objects.filter(
                estudante__usuario = self.request.user,
                data_termino__lt=datetime.date.today()
            )

            dados["estagios_orientador"] = Estagio.objects.filter(
                orientador__usuario=self.request.user,
                data_termino__lt=datetime.date.today()
            )

        return dados
