# Generated by Django 3.2.5 on 2021-07-12 04:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 12, 10, 22, 39, 307010)),
        ),
    ]