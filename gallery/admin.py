from django.contrib import admin
from .models import WorkGallery, GalleryImage
# Register your models here.
class GalleryImageInline(admin.TabularInline):
      model = GalleryImage
      extra = 1
      max_num = 5 

@admin.register(WorkGallery)
class WorkGalleryAdmin(admin.ModelAdmin):
      list_display = ('title', 'location', 'created_at')
      search_fields = ('title', 'location')
      inlines = [GalleryImageInline]


