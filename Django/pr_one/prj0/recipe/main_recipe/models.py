from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField("")
    price = models.DecimalField(decimal_places=2, max_digits = 50)
    image = models.ImageField(upload_to='recipes/')
    date_created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name