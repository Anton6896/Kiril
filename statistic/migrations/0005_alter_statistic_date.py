# Generated by Django 3.2.3 on 2021-06-06 16:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0004_alter_statistic_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistic',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 6, 16, 43, 34, 565962, tzinfo=utc)),
        ),
    ]
