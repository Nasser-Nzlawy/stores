from django.db import models
# Create your models here.
class slideimage(models.Model):
    slideimage_name=models.CharField(max_length=50 , unique=True)
    description = models.TextField(max_length=300 , blank=True)
    slideimage_image =models.ImageField (upload_to= 'photos/slideimages', blank=True)

    class Meta:
        verbose_name ='slideimage'
        verbose_name_plural ='slideimages' 

    
            
    def __str__(self):
        return self.slideimage_name

