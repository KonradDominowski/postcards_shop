# Generated by Django 4.1.2 on 2022-10-18 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='photos/')),
                ('country', models.CharField(max_length=32)),
                ('latitude', models.CharField(max_length=16)),
                ('latituderef', models.CharField(max_length=1)),
                ('longitude', models.CharField(max_length=16)),
                ('longituderef', models.CharField(max_length=1)),
            ],
        ),
    ]
