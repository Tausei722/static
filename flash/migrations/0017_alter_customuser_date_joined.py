# Generated by Django 5.1.1 on 2024-09-11 07:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flash', '0016_alter_customuser_date_joined_alter_movie_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 11, 16, 3, 37, 447377)),
        ),
    ]
