# Generated by Django 3.0.5 on 2020-04-30 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_useravatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='user/%Y/%m/%d/'),
        ),
        migrations.DeleteModel(
            name='UserAvatar',
        ),
    ]
