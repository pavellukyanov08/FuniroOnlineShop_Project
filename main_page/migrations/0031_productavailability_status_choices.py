# Generated by Django 4.2.4 on 2023-10-05 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0030_alter_productavailability_availability_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='productavailability',
            name='status_choices',
            field=models.CharField(max_length=12, null=True, verbose_name='Название статуса'),
        ),
    ]
