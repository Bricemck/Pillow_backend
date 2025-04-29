from django.db import models

class User(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    isRealtor = models.BooleanField(default=False)
    userId = models.ForeignKey


class Listing(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='listing_images/', blank=True, null=True)
    bedrooms = models.IntegerField 
    listed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')