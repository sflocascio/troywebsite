from django.db import models
from tinymce import HTMLField

# Create your models here.
class AboutSection(models.Model):
    title = models.CharField(max_length=255)
    
    subheading = models.CharField(max_length=255)
    image = models.ImageField(upload_to='test_image', blank=True)
    body = models.TextField(max_length=500, blank=False)

class Post(models.Model):
    title = models.CharField(max_length=120)
    
    content = HTMLField('Content')
    draft = models.BooleanField(default=False)
    date = models.IntegerField(null=True)
    year = models.IntegerField(null=True)
    month = models.CharField(max_length=255,null=True)
    image = models.ImageField(upload_to='test_image', blank=True)

    def __str__(self):
        return self.title




 