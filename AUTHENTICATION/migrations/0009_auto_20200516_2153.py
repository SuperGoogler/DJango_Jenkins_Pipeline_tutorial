# Generated by Django 3.0.5 on 2020-05-16 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AUTHENTICATION', '0008_userprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='Photo',
            field=models.ImageField(null=True, upload_to='documents/%Y/%m/%d/'),
        ),
    ]
