# Generated by Django 3.0.5 on 2020-04-07 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discount',
            old_name='fix',
            new_name='fix_price',
        ),
    ]
