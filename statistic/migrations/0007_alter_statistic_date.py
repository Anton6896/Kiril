# Generated by Django 3.2.3 on 2021-06-06 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0006_alter_statistic_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistic',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
