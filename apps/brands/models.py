from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=256)
    image = models.FileField(upload_to='home/brands')
    def __str__(self):
        return self.name