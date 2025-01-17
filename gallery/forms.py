from django import forms
from .models import WorkGallery, GalleryImage

class WorkGalleryForm(forms.ModelForm):
    class Meta:
        model = WorkGallery
        fields = ['title', 'location', 'description']

class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ['image', 'order']

        