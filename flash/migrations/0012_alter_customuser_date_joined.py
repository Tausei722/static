# Generated by Django 5.1.1 on 2024-09-10 18:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flash', '0011_alter_customuser_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 11, 3, 44, 57, 565086)),
        ),
    ]
