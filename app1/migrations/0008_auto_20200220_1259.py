# Generated by Django 2.2.6 on 2020-02-20 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20200220_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='price',
            field=models.DecimalField(decimal_places=4, default=9536.25, max_digits=14),
        ),
    ]
