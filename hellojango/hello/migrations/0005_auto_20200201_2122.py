# Generated by Django 3.0.2 on 2020-02-01 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0004_auto_20200201_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetrack',
            name='spent_time',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
