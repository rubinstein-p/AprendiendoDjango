# Generated by Django 4.0.4 on 2022-05-15 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiendaApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('categoria', models.ManyToManyField(to='tiendaApp.categoria')),
            ],
        ),
    ]
