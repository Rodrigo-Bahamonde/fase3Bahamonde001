# Generated by Django 2.2.3 on 2020-11-28 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sesion', '0005_auto_20201128_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
