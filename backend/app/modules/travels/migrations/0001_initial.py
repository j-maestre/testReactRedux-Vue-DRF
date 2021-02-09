# Generated by Django 3.0.2 on 2021-02-09 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0003_profile_favorites'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travels',
            fields=[
                ('slug', models.SlugField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('numPassengers', models.CharField(default='2', max_length=11)),
                ('date', models.CharField(max_length=200)),
                ('startTime', models.CharField(max_length=200)),
                ('finishTime', models.CharField(max_length=200)),
                ('city', models.CharField(default='no where', max_length=200)),
                ('ubication', models.CharField(default='no where', max_length=200)),
                ('postalCode', models.CharField(default='0000', max_length=200)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='travels', to='profiles.Profile')),
            ],
        ),
    ]
