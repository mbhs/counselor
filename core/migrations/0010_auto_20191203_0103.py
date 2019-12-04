# Generated by Django 2.2.4 on 2019-12-03 01:03

from django.db import migrations, models
from django.utils import timezone

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20191203_0102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='dateandtime',
        ),
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(default=timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.TimeField(default=timezone.now),
            preserve_default=False,
        ),
    ]
