# Generated by Django 3.1.5 on 2021-05-28 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='join_date',
        ),
    ]
