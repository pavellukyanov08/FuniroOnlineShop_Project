# Generated by Django 4.2.7 on 2023-11-15 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0060_product_favorites_statuses'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='favorites_statuses',
            new_name='favorite_status',
        ),
    ]
