from django.db import models



# Create your models here.

class News(models.Model):
    Email = models.EmailField(null=True, blank=True)

    def __str__(self):
    	return str(self.id)