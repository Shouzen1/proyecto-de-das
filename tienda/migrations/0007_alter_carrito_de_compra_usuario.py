# Generated by Django 5.0.6 on 2024-07-08 04:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0006_carrito_de_compra_producto_carrito'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito_de_compra',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='carritos', to=settings.AUTH_USER_MODEL),
        ),
    ]
