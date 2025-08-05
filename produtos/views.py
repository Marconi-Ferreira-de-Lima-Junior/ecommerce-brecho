from django.shortcuts import render, redirect, get_object_or_404
from django.utils.http import urlencode
from urllib.parse import quote
from .models import Produto
from django.core.paginator import Paginator  

def lista_produtos(request):
    query = request.GET.get('q')  # Pega o valor do campo de busca (q)
    
    produtos = Produto.objects.all().order_by('-criado_em')  # Todos os produtos ordenados do mais novo para o mais antigo

    if query:
        produtos = produtos.filter(nome__icontains=query)  
        # Se o usuário digitou algo, filtra os produtos cujo nome contenha esse texto (sem diferenciar maiúsculas/minúsculas)

    # Paginador: quebra a lista em partes
    paginator = Paginator(produtos, 9)  # Mostra 9 produtos por página
    page_number = request.GET.get('page')  # Verifica em qual página o usuário está
    page_obj = paginator.get_page(page_number)  # Retorna a página atual com os produtos corretos

    return render(request, 'produtos/lista_produtos.html', {
        'page_obj': page_obj,
        'produtos': page_obj,  # A mesma variável usada no template
    })


def whatsapp_redirect(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)#Redireciona para o WhatsApp com mensagem pré-formatada sobre o produto Inclui tratamento de erro caso o produto não exista
    # Formata a mensagem com os dados do produto
    mensagem = (
        f"Olá! Vi o produto *{produto.nome}* no Brechó Moda Renascida.\n\n" # * para ficar em negrito
        f"• *Preço:* R$ {produto.preco:.2f}\n"
        f"• *Descrição:* {produto.descricao}\n\n"
        "Este produto ainda está disponível?"
    )
    
    # Codifica a mensagem para URL
    mensagem_codificada = quote(mensagem) #quote evita que o sql interprete as aspas simples como delimitador de campo ou operador
    
    # Monta a URL do WhatsApp
    whatsapp_url = f"https://wa.me/5581999002431?text={mensagem_codificada}"
    
    return redirect(whatsapp_url)