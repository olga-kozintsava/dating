# Generated by Django 3.0.5 on 2020-04-30 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200429_1037'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAvatar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('avatar', models.ImageField(blank=True, upload_to='users/%Y/%m/%d/')),
                ('avatar_base64', models.TextField(blank=True, default=None, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avatar', to='accounts.UserProfile')),
            ],
        ),
    ]