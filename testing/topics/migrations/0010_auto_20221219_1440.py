# Generated by Django 3.2.16 on 2022-12-19 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0009_auto_20221219_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertest',
            name='right_answers',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='usertest',
            name='wrong_answers',
            field=models.IntegerField(default=0),
        ),
    ]