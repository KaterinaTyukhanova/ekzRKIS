# Generated by Django 5.0 on 2023-12-23 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tovar',
            name='user',
        ),
    ]
