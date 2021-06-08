# Generated by Django 3.2.3 on 2021-06-08 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0008_statistic_statistic_date_c46ea3_idx'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistic',
            name='clicks',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='statistic',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='statistic',
            name='views',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
