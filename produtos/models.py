from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True) #indica que a descrição é opicional 
    preco = models.DecimalField(max_digits=7,decimal_places=2)
    imagem = models.ImageField(upload_to='produto/')
    criado_em = models.DateTimeField(auto_now_add=True) #Todas as vezes que for adicionado um produto, salva automatico a data

    def __str__(self):
        return self.nome
    
