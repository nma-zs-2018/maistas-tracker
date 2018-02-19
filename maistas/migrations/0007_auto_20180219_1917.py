# Generated by Django 2.0.2 on 2018-02-19 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maistas', '0006_auto_20180219_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='main',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='current_delivery_lat',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='current_delivery_long',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='deliver_to_lat',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='deliver_to_long',
            field=models.FloatField(default=0),
        ),
    ]