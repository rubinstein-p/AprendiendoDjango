# Generated by Django 4.0.4 on 2022-05-15 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tiendaApp', '0002_productos'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productos',
            options={'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
        migrations.AddField(
            model_name='productos',
            name='disponivilidad',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='productos',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='tienda'),
        ),
        migrations.RemoveField(
            model_name='productos',
            name='categoria',
        ),
        migrations.AddField(
            model_name='productos',
            name='categoria',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='tiendaApp.categoria'),
            preserve_default=False,
        ),
    ]
