from django.db import models
from django.contrib.auth.models import User


class Food(models.Model):
    def __str__(self):
        return self.food_name

    food_name = models.CharField(max_length=100)


class Order(models.Model):
    deliver_by = models.ForeignKey(User, default=None, related_name='deliver_by', on_delete=models.DO_NOTHING)
    deliver_to = models.ForeignKey(User, default=None, related_name='deliver_to', on_delete=models.DO_NOTHING)
    deliver_to_lat = models.FloatField(default=0)
    deliver_to_long = models.FloatField(default=0)
    current_delivery_lat = models.FloatField(default=0)
    current_delivery_long = models.FloatField(default=0)
    food = models.ForeignKey(Food, default=None, on_delete=models.DO_NOTHING)
    quantity = models.PositiveSmallIntegerField(default=0)
    main = models.BooleanField(default=False)
