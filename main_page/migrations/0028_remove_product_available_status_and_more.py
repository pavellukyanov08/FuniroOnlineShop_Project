# Generated by Django 4.2.4 on 2023-10-05 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0027_alter_productavailability_availability_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='available_status',
        ),
        migrations.AddField(
            model_name='product',
            name='product_availability',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_page.productavailability', verbose_name='Наличие'),
        ),
    ]
