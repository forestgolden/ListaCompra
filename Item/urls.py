from django.contrib import admin
from django.urls import path
from .views import listar_item, listar_tipo_item, novo_tipo_item, atualizar_tipo_item, excluir_tipo_item

urlpatterns = [
    path('listar_item/', listar_item),
    path('listar_tipo_item/', listar_tipo_item, name="lista_tipo_item"),
    path('novo_tipo_item/', novo_tipo_item, name="novo_tipo_item"),
    path('atualizar/<int:id>/', atualizar_tipo_item, name="autalizar_tipo_item"),
    path('excluir/<int:id>/', excluir_tipo_item, name="excluir_tipo_item"),

]
