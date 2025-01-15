from django.db import models

# Create your models here.
from django.core.validators import MaxValueValidator
class WorkGallery(models.Model):
      title = models.CharField(max_length=100)
      location = models.CharField(max_length=100)
      description = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)

      def __str__(self):
            return self.title
      
      class Meta:
            verbose_name_plural = "Work Galleries"

class GalleryImage(models.Model):
      gallery = models.ForeignKey(WorkGallery, related_name='images', on_delete=models.CASCADE)
      image = models.ImageField(upload_to='gallery/')
      order = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)])

      class Meta:
            ordering = ['order']

