# Generated by Django 5.0.6 on 2024-07-02 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_rename_stock_producto_cantidad'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CategoriaProd',
            new_name='CategoriadeProductos',
        ),
        migrations.AlterModelOptions(
            name='categoriadeproductos',
            options={'verbose_name': 'categoriadeproductos', 'verbose_name_plural': 'categoriasdeproductos'},
        ),
    ]