# Generated by Django 2.2.3 on 2020-11-28 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sesion', '0008_auto_20201128_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='tipo',
            field=models.CharField(choices=[('Admin', 'Admin'), ('User', 'User')], default='User', max_length=6),
        ),
    ]
