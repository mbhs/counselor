# Generated by Django 2.1.3 on 2019-06-16 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='textpage',
            name='numId',
            field=models.IntegerField(default=0),
        ),
    ]
