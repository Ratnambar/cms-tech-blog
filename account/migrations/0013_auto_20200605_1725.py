# Generated by Django 2.2.5 on 2020-06-05 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_auto_20200605_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile/'),
        ),
    ]
