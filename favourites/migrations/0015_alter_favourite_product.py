# Generated by Django 4.2.4 on 2023-09-30 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0014_alter_product_category'),
        ('favourites', '0014_remove_favourite_description_remove_favourite_height_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favourite',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.product'),
        ),
    ]
