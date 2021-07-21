from django.db import models
from Item.models import ModelItem
# Create your models here.
class ModelLista(models.Model):
    id = models.AutoField(primary_key=True)
    nome_lista = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_lista

class ModelItemLista(models.Model):
    id = models.AutoField(primary_key=True)
    lista_tipo = models.ForeignKey(ModelLista, verbose_name="Tipo da Lista", on_delete=models.CASCADE)
    lista_item = models.ForeignKey(ModelItem, verbose_name="Item da Lista", on_delete=models.CASCADE)
    quantidade = models.IntegerField()
