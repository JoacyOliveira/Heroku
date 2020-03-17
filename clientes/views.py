from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .forms import ProdutoForm
from django.contrib.auth.decorators import login_required


@login_required()
def lista_produtos(request):
    termo_busca = request.GET.get('pesquisa', None)
    if termo_busca:
        produtos = Produto.objects.all()
        produtos = produtos.filter(nome__icontains=termo_busca) or produtos.filter(modelo__icontains=termo_busca)
    else:
        produtos = Produto.objects.all()

    return render(request, 'list_product.html', {'produto': produtos})


@login_required()
def criar_produto(request):
    form = ProdutoForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = ProdutoForm()
    return render(request, 'create_product.html', {'form': form})


@login_required()
def update(request, id):
    produto = get_object_or_404(Produto, pk=id)
    form = ProdutoForm(request.POST or None, request.FILES or None, instance=produto)
    if form.is_valid():
        form.save()
        return redirect('list')
    return render(request, 'update_product.html', {'form': form})


@login_required()
def delete(request, id):
    produto = get_object_or_404(Produto, pk=id)
    form = ProdutoForm(request.POST or None, request.FILES or None, instance=produto)
    if request.method == 'POST':
        produto.delete()
        return redirect('list')
    return render(request, 'delete_product.html', {'produto': produto})
