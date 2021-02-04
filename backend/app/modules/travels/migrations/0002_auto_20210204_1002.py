# Generated by Django 3.0.2 on 2021-02-04 10:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='travels',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='travels',
            name='city',
            field=models.CharField(default='no where', max_length=200),
        ),
        migrations.AddField(
            model_name='travels',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 2, 4, 10, 1, 52, 847321, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='travels',
            name='date',
            field=models.CharField(default=datetime.datetime(2021, 2, 4, 10, 2, 5, 971922, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='travels',
            name='finishTime',
            field=models.CharField(default=datetime.datetime(2021, 2, 4, 10, 2, 10, 871013, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='travels',
            name='numPassengers',
            field=models.CharField(default=2, max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='travels',
            name='postalCode',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='travels',
            name='startTime',
            field=models.CharField(default=datetime.datetime(2021, 2, 4, 10, 2, 51, 102322, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='travels',
            name='ubication',
            field=models.CharField(default='no where', max_length=200),
        ),
    ]