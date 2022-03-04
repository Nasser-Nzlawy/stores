from django.db import models
from django.urls import reverse
from django.template import defaultfilters
# Create your models here.
class Brand(models.Model):
    Brand_name=models.CharField(max_length=50 , unique=True)
    slug = models.SlugField(max_length=50,allow_unicode=True, unique=True)
    description = models.TextField(max_length=300 , blank=True)
    Brand_image =models.ImageField (upload_to= 'photos/Brands', blank=True)

    class Meta:
        verbose_name ='Brand'
        verbose_name_plural ='Brands' 

    def get_url(self):
          return reverse('products_by_brand', args=[self.slug])
            
    def __str__(self):
        return self.Brand_name

