# Generated by Django 3.2.20 on 2023-07-13 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0005_alter_building_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='building',
            old_name='geographical_zone',
            new_name='L_G_A',
        ),
    ]
