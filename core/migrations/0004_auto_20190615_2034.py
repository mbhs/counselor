# Generated by Django 2.1.3 on 2019-06-16 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_textpage_numid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textpage',
            name='numId',
            field=models.IntegerField(),
        ),
    ]
