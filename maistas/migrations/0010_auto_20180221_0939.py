# Generated by Django 2.0.2 on 2018-02-21 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maistas', '0009_auto_20180221_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='deliver_to_lat',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='deliver_to_long',
            field=models.FloatField(default=0, null=True),
        ),
    ]
