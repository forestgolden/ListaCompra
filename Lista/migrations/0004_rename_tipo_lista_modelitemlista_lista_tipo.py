# Generated by Django 3.2.5 on 2021-07-21 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lista', '0003_alter_modelitemlista_lista_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modelitemlista',
            old_name='tipo_lista',
            new_name='lista_tipo',
        ),
    ]
