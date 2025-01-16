from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.
from .models import WorkGallery
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
class GalleryListView(ListView):
      model = WorkGallery
      template_name = 'gallery/our_work.html'
      context_object_name = 'galleries'
      ordering = ['-created_at']

class GalleryDetailView(DetailView):
      model = WorkGallery
      template_name = 'gallery/detail.html'
      context_object_name = 'gallery'

      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['images'] = self.object.images.all()
            return context 

class GalleryDeleteView(DeleteView):
      template_name = 'gallery/delete.html'
      model = WorkGallery
      success_url = reverse_lazy('our_work')

class GalleryCreateView(LoginRequiredMixin, CreateView):
      model = WorkGallery
      template_name = 'gallery/create.html'
      fields = ['title', 'location', 'description']
      success_url = reverse_lazy('our_work')

