# Generated by Django 2.2.5 on 2020-06-05 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_auto_20200605_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='display_name',
            field=models.CharField(db_index=True, default='Add your name', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile/default.jpg', upload_to='profile/'),
        ),
    ]
