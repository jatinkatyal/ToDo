# Generated by Django 2.0 on 2018-01-02 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskAPI', '0007_auto_20180101_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='doneAt',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
