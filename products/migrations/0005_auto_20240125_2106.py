# Generated by Django 3.2.23 on 2024-01-25 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20240125_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stove_feature',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.stovefeature'),
        ),
        migrations.AlterField(
            model_name='product',
            name='window_feature',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.windowfeature'),
        ),
    ]
