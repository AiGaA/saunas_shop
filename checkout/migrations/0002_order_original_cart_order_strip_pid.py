# Generated by Django 4.1 on 2024-03-28 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='original_cart',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='strip_pid',
            field=models.CharField(default='', max_length=254),
        ),
    ]
