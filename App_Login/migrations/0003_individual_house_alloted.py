# Generated by Django 3.1 on 2022-12-11 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0002_individual_theme_interest'),
    ]

    operations = [
        migrations.AddField(
            model_name='individual',
            name='house_alloted',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
