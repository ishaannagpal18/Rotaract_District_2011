# Generated by Django 3.1 on 2022-12-19 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0003_individual_house_alloted'),
    ]

    operations = [
        migrations.AddField(
            model_name='individual',
            name='rotaractor_or_interactor',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
