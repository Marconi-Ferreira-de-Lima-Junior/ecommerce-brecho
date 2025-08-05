from django.urls import path
from . import views

app_name = 'produtos'  # Adicionando namespace para organização

urlpatterns = [
    # Página principal - lista com os produtos
    path('', views.lista_produtos, name='lista_produtos'),
    
    # Redirecionamento para WhatsApp
    path('whatsapp/<int:produto_id>/', views.whatsapp_redirect, name='whatsapp_redirect'),
]
