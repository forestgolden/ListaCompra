# Generated by Django 3.2.5 on 2021-07-22 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Item', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelitem',
            name='imagem_item',
            field=models.ImageField(blank=True, null=True, upload_to='Itens'),
        ),
    ]
