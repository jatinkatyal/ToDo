# Generated by Django 2.0 on 2018-01-01 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskAPI', '0005_auto_20180101_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='createdAt',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='isDone',
            field=models.BooleanField(default=True),
        ),
    ]
