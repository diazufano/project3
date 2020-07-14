from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=20)
    user = models.CharField(max_length=20)
    paswd = models.CharField(max_length=6)
    tlf = models.CharField(max_length=9)

    def __str__(self):
        return f"{self.name} ({self.tlf})"
    