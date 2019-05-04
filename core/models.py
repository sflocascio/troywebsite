from django.db import models

# Create your models here.
class AboutSection(models.Model):
    title = models.CharField(max_length=255)
    
    subheading = models.CharField(max_length=255)
    image = models.ImageField(upload_to='test_image', blank=True)
    body = models.TextField(max_length=500, blank=False)



 