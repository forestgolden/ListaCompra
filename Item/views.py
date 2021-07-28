from django.shortcuts import render, redirect, get_object_or_404
from .models import ModelItem, ModelTipoItem
from .forms import TipoItemForm
# Create your views here.
def listar_item(request):
    itens = ModelItem.objects.all()
    return render(request, 'Item/listar_item.html', {'itens': itens})

def listar_tipo_item(request):
    tipo_itens = ModelTipoItem.objects.all()
    return render(request,'Tipo_Item/listar_tipo_item.html', {'tipo_itens': tipo_itens})

def novo_tipo_item(request):
    #Se tiver algo, começa preenchido, se não, começa vazio
    form = TipoItemForm(request.POST, None)
    if form.is_valid():
        form.save()
        return redirect('lista_tipo_item')
    return render(request, 'Tipo_Item/novo_tipo_item.html', {'form': form})

def atualizar_tipo_item(request, id):
    tipo_item = get_object_or_404(ModelTipoItem, pk=id)
    form = TipoItemForm(request.POST or None, instance=tipo_item)
    if form.is_valid():
        form.save()
        return redirect('lista_tipo_item')
    return render(request,'Tipo_Item/novo_tipo_item.html', {'form': form})

def excluir_tipo_item(request,id):
    tipo_item = get_object_or_404(ModelTipoItem, pk=id)
    form = TipoItemForm(request.POST or None, instance=tipo_item)
    if request.method == 'POST':
        tipo_item.delete()
        return redirect('lista_tipo_item')
    return render(request, 'Tipo_Item/excluir_tipo_item.html', {'form': form})