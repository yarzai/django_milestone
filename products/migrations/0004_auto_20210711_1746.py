# Generated by Django 3.2.5 on 2021-07-11 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210711_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='update',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
