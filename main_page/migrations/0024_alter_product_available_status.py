# Generated by Django 4.2.4 on 2023-10-05 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0023_alter_product_available_status_delete_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='available_status',
            field=models.CharField(choices=[('в наличии', 'В наличии'), ('не в наличии', 'Не в наличии')], db_index=True, max_length=12, null=True, verbose_name='Наличие'),
        ),
    ]
