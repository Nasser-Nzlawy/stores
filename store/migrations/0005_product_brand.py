# Generated by Django 3.1 on 2022-02-09 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0001_initial'),
        ('store', '0004_productgallery_reviewrating'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='brands.brand'),
            preserve_default=False,
        ),
    ]
