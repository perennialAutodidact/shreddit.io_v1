# Generated by Django 3.0.8 on 2020-08-03 03:31

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200802_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_image',
            field=models.ImageField(default='profile_images/default.jpg', upload_to=users.models.get_upload_path, verbose_name='profile image'),
        ),
    ]
