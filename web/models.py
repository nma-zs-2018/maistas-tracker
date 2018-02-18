from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    section = models.CharField(max_length=100)

    # image = models.ImageField(upload_to='student')
    def __str__(self):
        return self.name
