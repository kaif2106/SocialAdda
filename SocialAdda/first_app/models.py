from django.db import models

# Create your models here.
class Conf(models.Model):
    votes = models.IntegerField(default=0)
    text = models.TextField()
    visible = models.BooleanField(default=1)

    def __str__(self):
        return self.text

