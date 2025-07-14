from django.shortcuts import render
from .models import Produto

def lista_produtos(request):
    produtos = Produto.objects.all().order_by('-criado_em') #recupera todos os registros e ordena pela data que foi criado em ordem decrescente utilizando o " - " (menos)
    return render(request, 'produtos/lista_produtos.html', {'produtos':produtos})


