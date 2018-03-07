# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-07 18:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brew', '0006_auto_20180109_0535'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'Mensagem', 'verbose_name_plural': 'Mensagens'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Produto', 'verbose_name_plural': 'Produtos'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Perfil', 'verbose_name_plural': 'Perfis'},
        ),
        migrations.AlterModelOptions(
            name='request',
            options={'verbose_name': 'Pedido', 'verbose_name_plural': 'Pedidos'},
        ),
        migrations.AlterModelOptions(
            name='stock',
            options={'verbose_name': 'Estoque', 'verbose_name_plural': 'Estoques'},
        ),
        migrations.AlterField(
            model_name='message',
            name='email',
            field=models.EmailField(max_length=254, verbose_name=b'E-mail'),
        ),
        migrations.AlterField(
            model_name='message',
            name='name',
            field=models.CharField(max_length=128, verbose_name=b'Nome'),
        ),
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.TextField(verbose_name=b'Texto'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name=b'Descritivo'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=128, verbose_name=b'Nome'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(upload_to=b'', verbose_name=b'Foto'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(max_length=64, verbose_name=b'SKU'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.TextField(default=b'', verbose_name=b'Logradouro'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(default=b'', verbose_name=b'Descritivo'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='lat',
            field=models.FloatField(default=0.0, verbose_name=b'Latitude'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='lon',
            field=models.FloatField(default=0.0, verbose_name=b'Longitude'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(default=b'', max_length=128, verbose_name=b'Nome'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=64, verbose_name=b'Telefone'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(upload_to=b'', verbose_name=b'Foto'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='rank',
            field=models.IntegerField(verbose_name=b'Grau'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='side',
            field=models.IntegerField(verbose_name=b'Tipo'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=b'Cliente'),
        ),
        migrations.AlterField(
            model_name='request',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client', to='brew.Profile', verbose_name=b'Cliente'),
        ),
        migrations.AlterField(
            model_name='request',
            name='estimated',
            field=models.DateTimeField(verbose_name=b'Prazo'),
        ),
        migrations.AlterField(
            model_name='request',
            name='products',
            field=models.ManyToManyField(related_name='request_products', to='brew.Product', verbose_name=b'Produtos'),
        ),
        migrations.AlterField(
            model_name='request',
            name='provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='provider', to='brew.Profile', verbose_name=b'Fornecedor'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brew.Product', verbose_name=b'Produto'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=b'Fornecedor'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='quantity',
            field=models.IntegerField(verbose_name=b'Quantidade'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='value',
            field=models.FloatField(verbose_name=b'Valor'),
        ),
    ]
