# Generated by Django 2.2.5 on 2020-05-08 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_profile_show_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='show_name',
        ),
    ]