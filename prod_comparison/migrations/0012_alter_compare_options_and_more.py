# Generated by Django 4.2.4 on 2023-10-28 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prod_comparison', '0011_compare_cart_prods'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='compare',
            options={'ordering': ('products',), 'verbose_name': 'Сравнение товара', 'verbose_name_plural': 'Сравнение товаров'},
        ),
        migrations.RenameField(
            model_name='compare',
            old_name='cart_prods',
            new_name='cart_products',
        ),
        migrations.RenameField(
            model_name='compare',
            old_name='product',
            new_name='products',
        ),
    ]
