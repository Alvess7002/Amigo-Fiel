from django.http import Http404
from django.shortcuts import render

from .models import ProdutoPet


def index(request):
    # Listagem: busca todos os produtos cadastrados no banco
    produtos = ProdutoPet.objects.all()
    return render(request, "index.html", {"produtos": produtos})


def detalhe(request, id):
    # Detalhe: busca um único produto pelo id recebido na URL
    try:
        produto = ProdutoPet.objects.get(id=id)
    except ProdutoPet.DoesNotExist:
        raise Http404("Produto não encontrado")
    return render(request, "detalhe.html", {"produto": produto})
