# Generated by Django 4.2.4 on 2023-09-17 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0007_alter_product_discount_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='end_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='start_time',
            field=models.DateTimeField(null=True),
        ),
    ]
