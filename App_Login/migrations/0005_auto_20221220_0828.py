# Generated by Django 3.1 on 2022-12-20 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0004_individual_rotaractor_or_interactor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='individual',
            old_name='rotaractor_or_interactor',
            new_name='rotaractor_or_interactor_or_rotarian',
        ),
    ]
