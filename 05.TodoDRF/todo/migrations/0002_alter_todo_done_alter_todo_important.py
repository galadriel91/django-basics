# Generated by Django 4.2.1 on 2023-05-16 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='done',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='important',
            field=models.BooleanField(default=False),
        ),
    ]
