# Generated by Django 2.2.5 on 2020-05-19 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='profile/user.jpg', upload_to='profile/'),
        ),
    ]
