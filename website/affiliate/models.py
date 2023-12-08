from django.db import models
import datetime

# Create your models here.


class Product(models.Model):
#     name = models.CharField(max_length=255)
#     img = models.ImageField(upload_to='img')
#     rate = models.IntegerField()
#     info = models.TextField()
#     offer = models.BooleanField(default=False)
#
#     # Example datetime object
    date_obj = datetime.datetime(2023, 9, 27, 10, 37, 54, 770744, tzinfo=datetime.timezone.utc)
#
#     # Extract the year from the datetime object
    price = date_obj.year


#
#     # Now 'year' contains the numerical value (e.g., 2023) that can be assigned to the 'price' field
#
#
class Item(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='img')
    price = models.IntegerField()
    info = models.TextField()
    offer = models.BooleanField(default=False)
    link = models.TextField()
