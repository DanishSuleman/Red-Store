from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=256)
    featured_image = models.FileField(upload_to='products')
    description = models.TextField()
    price = models.FloatField()
    isFeatured = models.BooleanField()
    category = models.CharField(max_length=256)
    def __str__(self):
        return self.name