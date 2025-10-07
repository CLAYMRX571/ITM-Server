from django.db import models

class Payment(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    icons = models.ImageField(upload_to='icons', blank=True, null=True)

    def __str__(self):
        return self.name