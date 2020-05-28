# Generated by Django 2.2.6 on 2020-03-10 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_auto_20200302_0903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buy',
            name='Buy',
        ),
        migrations.AddField(
            model_name='buy',
            name='Buy_cash',
            field=models.DecimalField(decimal_places=8, default=0, max_digits=24),
        ),
        migrations.AddField(
            model_name='buy',
            name='buy_btc',
            field=models.DecimalField(decimal_places=8, default=0, max_digits=24),
        ),
        migrations.AlterField(
            model_name='buy',
            name='btc',
            field=models.DecimalField(decimal_places=8, default=0, max_digits=24),
        ),
        migrations.AlterField(
            model_name='buy',
            name='cash',
            field=models.DecimalField(decimal_places=8, default=10000.0, max_digits=24),
        ),
        migrations.AlterField(
            model_name='buy',
            name='price',
            field=models.DecimalField(decimal_places=4, default=8001.4467, max_digits=14),
        ),
    ]
