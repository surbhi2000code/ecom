# Generated by Django 3.1.5 on 2021-04-21 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lol', '0006_orderupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=''),
        ),
    ]
