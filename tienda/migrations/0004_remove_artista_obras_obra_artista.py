# Generated by Django 4.1.2 on 2024-07-08 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_voto_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artista',
            name='obras',
        ),
        migrations.AddField(
            model_name='obra',
            name='artista',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='obras', to='tienda.artista'),
            preserve_default=False,
        ),
    ]
