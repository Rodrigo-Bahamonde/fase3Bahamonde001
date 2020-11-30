# Generated by Django 2.2.3 on 2020-11-28 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sesion', '0006_auto_20201128_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='genero',
            field=models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=50),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='tipo',
            field=models.CharField(choices=[('Administrador', 'Admin'), ('Usuario', 'User')], default='User', max_length=6),
        ),
    ]