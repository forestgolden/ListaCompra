from django.db import models

# Create your models here.
class ModelTipoItem(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_nome = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo_nome

class ModelItem(models.Model):
    id = models.AutoField(primary_key=True)
    nome_item = models.CharField(max_length=100, unique=True)
    valor_item = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    imagem_item = models.ImageField(upload_to='Itens', null=True,blank=True)
    tipo_nome_item = models.ForeignKey(ModelTipoItem, verbose_name="Tipo Item", on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_item
