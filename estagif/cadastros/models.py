from django.db import models

# Create your models here.


class UnidadeConcedente(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=15)
    documento = models.CharField(max_length=18, help_text="Preencha com o CNPJ ou CPF (caso pessoa física)")
    atualizado_em = models.DateTimeField(auto_now=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return f"{self.nome} ({self.documento})"
    

class Responsavel(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=15)
    cpf = models.CharField(max_length=14)
    empresa = models.ForeignKey(
        UnidadeConcedente, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nome} ({self.telefone})"

