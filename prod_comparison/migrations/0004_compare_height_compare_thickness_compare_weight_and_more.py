# Generated by Django 4.2.4 on 2023-09-14 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prod_comparison', '0003_alter_compare_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='compare',
            name='height',
            field=models.CharField(max_length=10, null=True, verbose_name='Высота'),
        ),
        migrations.AddField(
            model_name='compare',
            name='thickness',
            field=models.CharField(max_length=10, null=True, verbose_name='Толщина'),
        ),
        migrations.AddField(
            model_name='compare',
            name='weight',
            field=models.CharField(max_length=10, null=True, verbose_name='Вес'),
        ),
        migrations.AddField(
            model_name='compare',
            name='width',
            field=models.CharField(max_length=10, null=True, verbose_name='Ширина'),
        ),
    ]
