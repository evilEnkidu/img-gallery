from django.urls import path
from .views import GalleryListView

urlpatterns = [
    path('gallery', GalleryListView.as_view(), name='our_work'),
] 