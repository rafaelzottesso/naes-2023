from django.db import models

# Importar a classe User do Django para fazer os relacionamentos
from django.contrib.auth.models import User


# Create your models here.
TIPOS_RELATORIO = [
    ('Parcial', 'Parcial'),
    ('Final', 'Final'),
]


class Campus(models.Model):
    nome = models.CharField(max_length=50)

    atualizado_em = models.DateTimeField(auto_now=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome}"
    
    class Meta:
        verbose_name_plural = "Campi"


class Curso(models.Model):
    nome = models.CharField(max_length=50)
    campus = models.ForeignKey(Campus, on_delete=models.PROTECT)

    atualizado_em = models.DateTimeField(auto_now=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome}"


class Estudante(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14, verbose_name="CPF", unique=True)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    matricula = models.CharField(max_length=15, verbose_name="matrícula")
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)
    campus = models.ForeignKey(Campus, on_delete=models.PROTECT)
    
    # A relação com o usuário é um para um, ou seja, um usuário só pode ter um estudante e vice versa
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    
    atualizado_em = models.DateTimeField(auto_now=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} ({self.matricula})"


class Servidor(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14, verbose_name="CPF", unique=True)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    siape = models.CharField(max_length=15, verbose_name="SIAPE")
    campus = models.ForeignKey(Campus, on_delete=models.PROTECT)

    # A relação com o usuário é um para um, ou seja, um usuário só pode ter um servidor e vice versa
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    atualizado_em = models.DateTimeField(auto_now=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} ({self.siape})"
    
    class Meta:
        verbose_name_plural = "Servidores"


class UnidadeConcedente(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=15)
    documento = models.CharField(max_length=18, help_text="Preencha com o CNPJ ou CPF (caso pessoa física)")

    cep = models.CharField(max_length=10, verbose_name="CEP")
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=20, verbose_name="Número", null=True, blank=True)
    bairro = models.CharField(max_length=50, null=True, blank=True)
    cidade = models.CharField(max_length=50)



    atualizado_em = models.DateTimeField(auto_now=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return f"{self.nome} ({self.documento})"
    
    class Meta:
        verbose_name_plural = "Unidades Concedentes"
    

class Responsavel(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=15)
    cpf = models.CharField(max_length=14, verbose_name="CPF", unique=True)
    empresa = models.ForeignKey(UnidadeConcedente, on_delete=models.PROTECT)

    atualizado_em = models.DateTimeField(auto_now=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} ({self.telefone})"

    class Meta:
        verbose_name_plural = "Responsáveis"


class Intermediario(models.Model):
    nome = models.CharField(max_length=50)

    atualizado_em = models.DateTimeField(auto_now=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome}"
    
    class Meta:
        verbose_name = "Intermediário"


class Situacao(models.Model):
    nome = models.CharField(max_length=50)

    atualizado_em = models.DateTimeField(auto_now=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome}"
    
    class Meta:
        verbose_name = "Situação"
        verbose_name_plural = "Situações"


class Estagio(models.Model):
    estudante = models.ForeignKey(Estudante, on_delete=models.PROTECT)
    intermediario = models.ForeignKey(Intermediario, on_delete=models.PROTECT, verbose_name="intermediário")
    unidade_concedente = models.ForeignKey(UnidadeConcedente, on_delete=models.PROTECT)
    responssvel_empresa = models.ForeignKey(Responsavel, on_delete=models.PROTECT, verbose_name="responsável na empresa")
    orientador = models.ForeignKey(Servidor, on_delete=models.PROTECT)
    data_inicio = models.DateTimeField(verbose_name="data de início")
    data_termino = models.DateTimeField(verbose_name="data de término", null=True)
    ch_semanal = models.IntegerField(verbose_name="carga horária semanal")
    situacao = models.ForeignKey(Situacao, on_delete=models.PROTECT, verbose_name="situação")
    observacoes = models.TextField(blank=True, null=True, verbose_name="observações")
    data_protocolo = models.DateTimeField(auto_now_add=True)

    atualizado_em = models.DateTimeField(auto_now=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    # A relação ForeignKey é um pra muitos, ou seja, o usuário pode cadastrar vários estágios
    cadastrado_por = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"[#{self.id}] {self.estudante.nome} ({self.data_inicio} - {self.unidade_concedente.nome})"
    
    class Meta:
        verbose_name = "Estágio"
        ordering = ['-data_inicio']


class Historico(models.Model):
    estagio = models.ForeignKey(Estagio, on_delete=models.PROTECT, verbose_name="estágio")
    situacao = models.ForeignKey(Situacao, on_delete=models.PROTECT, verbose_name="situação")

    atualizado_em = models.DateTimeField(auto_now=True)
    atualizado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome}"
    
    class Meta:
        verbose_name = "Histórico"


class Relatorio(models.Model):
    estagio = models.ForeignKey(Estagio, on_delete=models.PROTECT, verbose_name="estágio")
    data_inicio = models.DateTimeField(verbose_name="data de início")
    data_termino = models.DateTimeField(verbose_name="data de término")
    tipo = models.CharField(max_length=20, choices=TIPOS_RELATORIO)
    entregue = models.BooleanField(default=False, help_text="O aluno já entregou o relatório.")
    data_cadastro = models.DateTimeField()

    atualizado_em = models.DateTimeField(auto_now=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    
    # A relação ForeignKey é um pra muitos, ou seja, o usuário pode cadastrar vários relatórios
    cadastrado_por = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nome}"
    
    class Meta:
        verbose_name = "Relatório"




class Produto(models.Model):
    nome = models.CharField(max_length=50)
    valor = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f"{self.nome} - R${self.valor}"
    

class Venda(models.Model):
    cliente = models.CharField(max_length=50)
    valor_total = models.DecimalField(decimal_places=2, max_digits=10)
    forma_pagamento = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cliente} - R${self.valor_total}"


class ProdutoVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.PROTECT)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.IntegerField(default=1)
    valor = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f"#{self.venda.pk} ~ {self.quantidade} x {self.produto}"


class Carinho(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantidade} x {self.produto}"
