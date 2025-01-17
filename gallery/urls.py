from django.urls import path
from .views import GalleryListView, GalleryDetailView, WorkGalleryUpdateView, GalleryImageUpdateView, GalleryCreateView, AddGalleryImagesView, GalleryDeleteView



urlpatterns = [
    path('gallery', GalleryListView.as_view(), name='our_work'),
    path('gallery/<int:pk>/', GalleryDetailView.as_view(), name='gallery_detail'),
    path('workgallery/<int:pk>/update/', WorkGalleryUpdateView.as_view, name='description_update'),
    path('galleryimage/int<int:pk>/update', GalleryImageUpdateView.as_view(), name='image_update'),
    path('gallery/create/', GalleryCreateView.as_view(), name='add-to-gallery'),
    path('gallery/<int:pk>/add-images/', AddGalleryImagesView.as_view(), name='add-gallery-images'),
   path('gallery/<int:pk>/delete/', GalleryDeleteView.as_view(), name='gallery_delete'),
] 