# Generated by Django 2.1.2 on 2018-11-12 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20181109_1023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock_daily',
            name='turnoverratio',
        ),
    ]
