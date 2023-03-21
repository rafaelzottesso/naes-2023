# Generated by Django 4.1.5 on 2023-03-21 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UnidadeConcedente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=100)),
                ("telefone", models.CharField(max_length=15)),
                (
                    "documento",
                    models.CharField(
                        help_text="Preencha com o CNPJ ou CPF (caso pessoa física)",
                        max_length=18,
                    ),
                ),
                ("atualizado_em", models.DateTimeField(auto_now=True)),
                ("cadastrado_em", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Responsavel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=100)),
                ("telefone", models.CharField(max_length=15)),
                ("cpf", models.CharField(max_length=14)),
                (
                    "empresa",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="cadastros.unidadeconcedente",
                    ),
                ),
            ],
        ),
    ]
