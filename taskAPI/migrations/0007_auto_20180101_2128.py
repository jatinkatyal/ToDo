# Generated by Django 2.0 on 2018-01-01 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskAPI', '0006_auto_20180101_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='isDone',
            field=models.NullBooleanField(default=True),
        ),
    ]
