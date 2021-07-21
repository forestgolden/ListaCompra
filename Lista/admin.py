from django.contrib import admin
from .models import ModelLista, ModelItemLista
# Register your models here.
admin.site.register(ModelItemLista)
admin.site.register(ModelLista)