from django.db import models

# Create your models here.
class Terms(models.Model):
	definition = models.TextField()
	name = models.CharField(max_length = 100)


