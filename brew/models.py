from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    class Meta:
        verbose_name = 'Mensagem'
        verbose_name_plural = 'Mensagens'
    name = models.CharField(max_length=128, verbose_name='Nome')
    email = models.EmailField(verbose_name='E-mail')
    text = models.TextField(verbose_name='Texto')
    def __str__(self):
        return 'Mensagem de %s' % self.name

class Profile(models.Model):
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
    user = models.OneToOneField(User, verbose_name='Cliente')
    lat = models.FloatField(default=0.0, verbose_name='Latitude')
    lon = models.FloatField(default=0.0, verbose_name='Longitude')
    name = models.CharField(default="",max_length=128, verbose_name='Nome')
    description = models.TextField(default="", verbose_name='Descritivo')
    address = models.TextField(default="", verbose_name='Logradouro')
    photo = models.ImageField(verbose_name='Foto')
    phone = models.CharField(max_length=64, verbose_name='Telefone')
    side = models.IntegerField(verbose_name='Tipo')
    rank = models.IntegerField(verbose_name='Grau')
    def __str__(self):
        return self.name

class Product(models.Model):
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
    sku = models.CharField(max_length=64, verbose_name='SKU')
    name = models.CharField(max_length=128, verbose_name='Nome')
    description = models.TextField(verbose_name='Descritivo')
    photo = models.ImageField(verbose_name='Foto')
    def __str__(self):
        return self.name

class Stock(models.Model):
    class Meta:
        verbose_name = 'Estoque'
        verbose_name_plural = 'Estoques'
    key = models.ForeignKey(Product, verbose_name='Produto')
    provider = models.ForeignKey(User, verbose_name='Fornecedor')
    value = models.FloatField(verbose_name='Valor')
    quantity = models.IntegerField(verbose_name='Quantidade')
    def __str__(self):
        return 'Estoque de %s' % self.key

class Request(models.Model):
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
    client = models.ForeignKey(User, null=True, related_name="client", verbose_name='Cliente')
    provider = models.ForeignKey(User, null=True, related_name="provider", verbose_name='Fornecedor')
    products = models.ManyToManyField(Product, related_name="request_products", verbose_name='Produtos')
    estimated = models.DateTimeField(verbose_name='Prazo')
    def __str__(self):
        return 'Pedido de %s' % self.client
