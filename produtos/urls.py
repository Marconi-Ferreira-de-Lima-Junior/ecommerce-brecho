from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    # Página inicial
    path('', views.inicio, name='inicio'),

    # Lista de produtos
    path('produtos/', views.lista_produtos, name='lista_produtos'),

    # Páginas institucionais
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),

    # Redirecionamento WhatsApp
    path('whatsapp/<int:produto_id>/', views.whatsapp_redirect, name='whatsapp_redirect'),
]
