# Generated by Django 3.2.5 on 2021-07-11 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210711_1746'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='update',
            new_name='updated',
        ),
    ]
