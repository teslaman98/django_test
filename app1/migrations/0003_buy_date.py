# Generated by Django 2.2.6 on 2020-02-20 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20200219_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
