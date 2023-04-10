# Generated by Django 4.2 on 2023-04-10 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Burger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='햄버거 이름')),
                ('price', models.IntegerField(verbose_name='햄버거 가격')),
                ('calories', models.IntegerField(verbose_name='햄버거 칼로리')),
            ],
        ),
    ]