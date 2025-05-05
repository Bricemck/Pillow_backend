from django.db import models
from django.contrib.auth.models import AbstractUser

class User(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    isRealtor = models.BooleanField(default=False)
    


class Listing(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='listing_images/', blank=True, null=True)
    bedrooms = models.IntegerField(default=1)
    #listed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')

# CREATE TABLE pillow_backend_user(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(25),
#     password VARCHAR(25),
#     isRealtor BOOLEAN
# );

# CREATE TABLE pillow_backend_listing(
#     id SERIAL PRIMARY KEY,
#     title VARCHAR(50),
#     price INT,
#     image VARCHAR(100),
#     bedrooms INT,
#     listed_by INT,
#     FOREIGN KEY (listed_by) REFERENCES pillow_backend_user(id)
# );