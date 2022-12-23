from django.db import models

class StoreImage(models.Model):
    image = models.ImageField()
