from django.db import models

# Create your models here.
class Team_Member(models.Model):
    name = models.CharField(max_length=256)
    designation = models.CharField(max_length=256)
    image = models.FileField(upload_to='about/team_members')
    facebook = models.TextField(default="https://www.facebook.com/groups/407961892610345/")
    linkedIn = models.TextField(default="https://www.linkedin.com/company/javascript-developer")
    twitter = models.TextField(default="https://twitter.com/javascript_dev_")
    def __str__(self):
        return self.name
    