# Generated by Django 3.2.3 on 2021-06-06 16:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0003_auto_20210606_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistic',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 6, 16, 42, 6, 37115)),
        ),
    ]
