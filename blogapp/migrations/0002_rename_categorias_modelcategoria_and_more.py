# Generated by Django 4.0.4 on 2022-05-14 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categorias',
            new_name='modelCategoria',
        ),
        migrations.AlterModelOptions(
            name='modelcategoria',
            options={'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
    ]