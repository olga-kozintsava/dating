# Generated by Django 3.0.5 on 2020-05-05 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_userlike'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userlike',
            old_name='vote',
            new_name='like',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='img/rabbit-vector-26.jpg', upload_to='user/%Y/%m/%d/'),
        ),
    ]