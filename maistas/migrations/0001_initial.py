# Generated by Django 2.0.2 on 2018-02-19 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deliver_to_lat', models.FloatField()),
                ('deliver_to_long', models.FloatField()),
                ('current_delivery_lat', models.FloatField()),
                ('current_delivery_long', models.FloatField()),
                ('deliver_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='deliver_by', to=settings.AUTH_USER_MODEL)),
                ('deliver_to', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='deliver_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
