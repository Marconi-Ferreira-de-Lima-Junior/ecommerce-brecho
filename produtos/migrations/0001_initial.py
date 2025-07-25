# Generated by Django 5.1.6 on 2025-06-22 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=7)),
                ('imagem', models.ImageField(upload_to='produto/')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
