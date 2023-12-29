from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class PhotoCategory(models.Model):
    category=models.CharField(max_length=10)
    
    def __str__(self):
        return self.category

class PhotoGallery(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=30)
    photo=models.ImageField(upload_to='photos/')
    description=models.TextField(max_length=2000)
    category=models.ForeignKey(PhotoCategory,on_delete=models.CASCADE)
    
    def __str__(self):
        return f" Title: {self.title} Category: {self.category}"
    
