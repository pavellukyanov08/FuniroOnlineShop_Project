# Generated by Django 4.2.4 on 2023-10-28 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favourites', '0018_remove_favourite_cart_prod'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favourite',
            options={'ordering': ('products',), 'verbose_name': 'Избранное', 'verbose_name_plural': 'Избранное'},
        ),
        migrations.RenameField(
            model_name='favourite',
            old_name='product',
            new_name='products',
        ),
    ]
