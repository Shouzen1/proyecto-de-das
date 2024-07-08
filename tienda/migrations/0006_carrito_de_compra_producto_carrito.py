# Generated by Django 5.0.6 on 2024-07-08 04:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0005_alter_voto_obra_alter_voto_usuario'),
        ('usuarios', '0004_remove_usuario_carrito_de_compra_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito_de_Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('comprado', 'Comprado')], max_length=100)),
                ('total', models.IntegerField(max_length=100)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='carritos', to='usuarios.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Producto_Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(max_length=100)),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.carrito_de_compra')),
                ('productos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.obra')),
            ],
        ),
    ]
