# Generated by Django 2.2.5 on 2020-07-22 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_auto_20200716_2048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='failities',
            new_name='facilities',
        ),
    ]
