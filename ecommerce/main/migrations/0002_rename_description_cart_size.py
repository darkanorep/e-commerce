# Generated by Django 4.1.5 on 2023-01-30 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='description',
            new_name='size',
        ),
    ]
