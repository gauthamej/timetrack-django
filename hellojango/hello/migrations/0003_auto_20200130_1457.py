# Generated by Django 3.0.2 on 2020-01-30 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_auto_20200130_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetrack',
            name='spent_time',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
