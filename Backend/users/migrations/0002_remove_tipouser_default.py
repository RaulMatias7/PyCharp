# Generated by Django 2.2.4 on 2020-09-27 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipouser',
            name='default',
        ),
    ]