from django.db import models

# Create your models here.
class Room(models.Model):
    #host
    #topic
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(default=0.0)
    rating = models.FloatField(default=0.0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

