# Generated by Django 3.1 on 2022-02-22 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='is_superadmin',
            new_name='is_superuser',
        ),
    ]
