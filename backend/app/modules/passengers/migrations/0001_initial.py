# Generated by Django 3.0.2 on 2021-02-04 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passengers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('travel_id', models.CharField(max_length=100)),
                ('user_id', models.CharField(max_length=100)),
            ],
        ),
    ]
