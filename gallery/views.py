from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from .models import WorkGallery
class GalleryListView(ListView):
      model = WorkGallery
      template_name = 'gallery/our_work.html'
      context_object_name = 'galleries'
      ordering = ['-created_at']
      