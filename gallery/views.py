from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import WorkGallery, GalleryImage
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import WorkGalleryForm, GalleryImageForm
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

class GalleryDeleteView(LoginRequiredMixin, DeleteView):
      template_name = 'gallery/delete.html'
      model = WorkGallery
      success_url = reverse_lazy('our_work')

class GalleryCreateView(LoginRequiredMixin, CreateView):
      model = WorkGallery
      template_name = 'gallery/create.html'
      fields = ['title', 'location', 'description']
      success_url = reverse_lazy('our_work')

class WorkGalleryUpdateView(LoginRequiredMixin, UpdateView):
      model = WorkGallery
      form_class = WorkGalleryForm
      template_name = 'gallery/description-update.html'
      success_url = reverse_lazy('our_work')

class GalleryImageUpdateView(LoginRequiredMixin, UpdateView):
      model = GalleryImage
      form_class = GalleryImageForm
      template_name = 'gallery/image-update.html'
      success_url = reverse_lazy('our_work')      
      
class AddGalleryImagesView(LoginRequiredMixin, View):
      template_name = 'gallery/add_gallery_images.html'

      def get(self, request, pk):
            gallery = get_object_or_404(WorkGallery, pk=pk)
            return render(request, self.template_name, {'gallery':gallery})

      def post(self, request, pk):
            gallery = get_object_or_404(WorkGallery, pk=pk)
            images = request.FILES.getlist('image')
            orders = request.POST.getlist('order')
            for image, order in zip(images, orders):
                  GalleryImage.objects.create(
                        gallery=gallery,
                        image=image,
                        order=order
                  )
            return redirect('gallery_detail', pk=gallery.pk)