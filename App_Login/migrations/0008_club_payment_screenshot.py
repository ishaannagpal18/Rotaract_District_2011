# Generated by Django 3.1 on 2022-12-20 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0007_club_rotary_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='payment_screenshot',
            field=models.ImageField(blank=True, upload_to='Payment_Screenshot'),
        ),
    ]