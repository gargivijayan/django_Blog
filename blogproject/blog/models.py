from django.db import models

# Create your models here.
class blog (models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='article_images/') 
    description=models.CharField(max_length=300)
    date=models.DateField()
    
     
