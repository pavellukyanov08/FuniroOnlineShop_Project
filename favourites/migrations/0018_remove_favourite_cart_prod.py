# Generated by Django 4.2.4 on 2023-10-28 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favourites', '0017_favourite_cart_prod'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favourite',
            name='cart_prod',
        ),
    ]
