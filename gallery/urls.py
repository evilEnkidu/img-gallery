from django.urls import path
from .views import GalleryListView, GalleryDetailView

urlpatterns = [
    path('gallery', GalleryListView.as_view(), name='our_work'),
    path('gallery/<int:pk>/', GalleryDetailView.as_view(), name='gallery_detail'),
] 