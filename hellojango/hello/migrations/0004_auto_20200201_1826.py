# Generated by Django 3.0.2 on 2020-02-01 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_auto_20200130_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetrack',
            name='spent_time',
            field=models.IntegerField(null=True),
        ),
    ]
