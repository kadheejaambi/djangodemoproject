from django.db import models

# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=30)
    desc=models.TextField(null=True)
    language=models.CharField(max_length=30)
    year=models.IntegerField()
    image=models.ImageField(upload_to="images")