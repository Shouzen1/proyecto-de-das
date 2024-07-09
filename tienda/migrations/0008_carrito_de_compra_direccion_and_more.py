# Generated by Django 5.0.6 on 2024-07-08 23:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0007_alter_carrito_de_compra_usuario'),
        ('usuarios', '0004_remove_usuario_carrito_de_compra_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito_de_compra',
            name='direccion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='carritos', to='usuarios.direccion'),
        ),
        migrations.AlterField(
            model_name='carrito_de_compra',
            name='total',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='producto_carrito',
            name='carrito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='tienda.carrito_de_compra'),
        ),
    ]