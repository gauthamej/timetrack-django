# Generated by Django 3.0.2 on 2020-02-04 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0012_projectform'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='revenue',
            name='date',
        ),
    ]
