from django.db import models
from django.contrib.auth.models import User


class Food(models.Model):
    def __str__(self):
        return self.food_name

    food_name = models.CharField(max_length=100)


class Order(models.Model):
    def __str__(self):
        returnstr = 'Delivery to ' + self.deliver_to.username + ' '
        if self.main:
            if self.deliver_by is None:
                returnstr += '(waiting)'
            else:
                returnstr += 'being delivered by ' + self.deliver_by.username
            returnstr += '*';

        return returnstr

    deliver_by = models.ForeignKey(User, default=None, related_name='deliver_by', on_delete=models.DO_NOTHING,
                                   null=True)
    deliver_to = models.ForeignKey(User, default=None, related_name='deliver_to', on_delete=models.DO_NOTHING,
                                   null=True)
    deliver_to_lat = models.FloatField(default=None, null=True)
    deliver_to_long = models.FloatField(default=None, null=True)
    current_delivery_lat = models.FloatField(default=None, null=True)
    current_delivery_long = models.FloatField(default=None, null=True)
    food = models.ForeignKey(Food, default=None, on_delete=models.DO_NOTHING)
    quantity = models.PositiveSmallIntegerField(default=0)
    main = models.BooleanField(default=False)
