# Generated by Django 3.0.2 on 2020-02-05 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0015_auto_20200205_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectform',
            name='hour_rate',
            field=models.IntegerField(null=True),
        ),
    ]
