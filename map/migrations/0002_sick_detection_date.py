# Generated by Django 3.1 on 2020-10-29 02:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sick',
            name='detection_date',
            field=models.DateField(default=datetime.datetime(2020, 10, 29, 2, 0, 39, 241608, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
