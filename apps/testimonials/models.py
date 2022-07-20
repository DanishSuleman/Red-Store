from django.db import models

# Create your models here.

class Testimonial(models.Model):
    name = models.CharField(max_length=256)
    image = models.FileField(upload_to='testimonials')
    testimony = models.TextField()
    def __str__(self):
        return self.name