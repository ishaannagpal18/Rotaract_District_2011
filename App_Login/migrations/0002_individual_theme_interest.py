# Generated by Django 3.1 on 2022-12-07 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='individual',
            name='theme_interest',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
