# Generated by Django 2.0 on 2018-01-01 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskAPI', '0002_auto_20180101_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='doneAt',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='taskId',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
