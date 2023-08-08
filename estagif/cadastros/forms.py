from dal import autocomplete
from django import forms
from .models import Estagio


class EstagioForm(forms.ModelForm):

    class Meta:
        model = Estagio
        fields = [
            "estudante", "intermediario", "unidade_concedente", "responssvel_empresa",
            "orientador", "data_inicio", "data_termino", "ch_semanal",
            "situacao", "observacoes",
        ]
        widgets = {
            
            # O campo "estudante" vai usar a seguinte URL para montar o campo
            # e fazer o filtro com base no que foi digitado
            "estudante" : autocomplete.ModelSelect2(
                url="buscar-estudante",
                attrs={
                    'data-placeholder': 'Informe o nome do estudante...',
                    'data-minimum-input-length': 3,
                }, # Fim do attrs
            ),  # Fim do autocomplete.ModelSelect2()
            
            # Autocomplete do orientador
            "orientador": autocomplete.ModelSelect2(
                url="buscar-orientador",
                attrs={
                    'data-placeholder': 'Informe o nome do orientador...',
                    'data-minimum-input-length': 3,
                },  # Fim do attrs
            ), # Fim do autocomplete.ModelSelect2()

        } # Fim do widgets

