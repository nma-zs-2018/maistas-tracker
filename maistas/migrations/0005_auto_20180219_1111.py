# Generated by Django 2.0.2 on 2018-02-19 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('maistas', '0004_auto_20180219_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='deliver_by',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='deliver_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='deliver_to',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='deliver_to', to=settings.AUTH_USER_MODEL),
        ),
    ]