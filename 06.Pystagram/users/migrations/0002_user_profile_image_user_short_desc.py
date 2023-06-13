# Generated by Django 4.2.2 on 2023-06-13 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='users/profile', verbose_name='프로필 사진'),
        ),
        migrations.AddField(
            model_name='user',
            name='short_desc',
            field=models.TextField(blank=True, verbose_name='짧은 소개'),
        ),
    ]
