# Generated by Django 4.0.5 on 2022-06-23 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valapp', '0002_profile_pic_center_profile_center'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=models.ImageField(default='default.png', upload_to='images/'),
        ),
    ]
