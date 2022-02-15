from django.db import models


# Create your models here.
class Conf(models.Model):
    votes = models.IntegerField(default=0)
    text = models.TextField()
    visible = models.BooleanField(default=False)
    visibleTime = models.TimeField(auto_now=True)

    class Meta:
        ordering = ['-visibleTime']
        
    def __str__(self):
        return self.text

