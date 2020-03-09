from django.db import models
import datetime


class Product (models.Model):
    name = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    image = models.ImageField()
    cat_id = models.IntegerField()