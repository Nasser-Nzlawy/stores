# Generated by Django 3.1 on 2022-02-09 23:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_product_audience_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='audience_price',
        ),
    ]
