# Generated by Django 2.2.1 on 2019-08-15 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20181112_0723'),
    ]

    operations = [
        migrations.CreateModel(
            name='stock_ban',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=100)),
                ('name', models.CharField(default='', max_length=20)),
                ('date', models.CharField(default='', max_length=20)),
                ('count', models.FloatField(default=None)),
                ('ratio', models.FloatField(default=None)),
            ],
        ),
    ]
