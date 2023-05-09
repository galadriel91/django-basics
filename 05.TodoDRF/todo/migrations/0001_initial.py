# Generated by Django 4.2.1 on 2023-05-09 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('important', models.BooleanField(default=False)),
                ('done', models.BooleanField(default=False)),
            ],
        ),
    ]
