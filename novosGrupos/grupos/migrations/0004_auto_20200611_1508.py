# Generated by Django 3.0.7 on 2020-06-11 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0003_auto_20200611_1459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='integrante',
            name='grupo',
        ),
        migrations.DeleteModel(
            name='Comeback',
        ),
        migrations.DeleteModel(
            name='Grupo',
        ),
        migrations.DeleteModel(
            name='Integrante',
        ),
    ]
