from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Category(models.Model):
    class Meta(object):
        db_table = 'categories'
    category_name = models.CharField(
        'name', blank=False, null=False, max_length=100, default='Horror'
    )
    category_image= CloudinaryField(
         blank=True
    )
  
    