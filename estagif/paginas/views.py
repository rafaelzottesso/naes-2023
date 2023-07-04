from cadastros.models import Estagio, Estudante, Servidor
from django.views.generic import TemplateView
import datetime


class IndexView(TemplateView):
    template_name = "paginas/index.html"
    
    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)

        if (self.request.user.is_authenticated):
            ###################
            # Exemplo de consulta mais bem elaborada... Explicado em aula
            ###################
            
            # cursos = Curso.objects.filter(campus__nome="Paranavaí")

            # relatorio = {}
            # for c in cursos:
            #     relatorio[c.pk] = Estagio.objects.filter(
            #         situacao__nome="Vigente",
            #         curso=c,
            #         data_inicio__year=2023
            #     ).count()

            # dados["cursos"] = cursos
            # dados["relatorios"] = relatorio
            

            dados["estagios_estudante"] = Estagio.objects.filter(
                estudante__usuario = self.request.user,
                #data_termino__lt=datetime.date.today()
            ).select_related("estudante", "orientador", "unidade_concedente")

            dados["estagios_orientador"] = Estagio.objects.filter(
                orientador__usuario=self.request.user,
                #data_termino__lt=datetime.date.today()
            ).select_related("estudante", "orientador", "unidade_concedente")

        return dados
