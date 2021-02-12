from django.db import models

# Create your models here.
class Advert(models.Model):
    banner = models.ImageField(upload_to="images/", null=True, blank=True)
    parent_page_visit = models.IntegerField(default=0)
    page_visit = models.IntegerField(default=0)
    impression_percentage = models.IntegerField(default=0)