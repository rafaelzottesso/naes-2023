# Generated by Django 4.1.5 on 2023-08-14 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("cadastros", "0004_produto_venda_produtovenda_carinho"),
    ]

    operations = [
        migrations.AddField(
            model_name="curso",
            name="campus",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="cadastros.campus",
            ),
            preserve_default=False,
        ),
    ]