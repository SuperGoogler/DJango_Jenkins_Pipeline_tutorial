# Generated by Django 3.0.5 on 2020-04-26 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AUTHENTICATION', '0005_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='District',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='Photo',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='State',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='country',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='uploaded_at',
        ),
    ]
