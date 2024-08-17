from django.urls import path,include
from.views import *

urlpatterns = [
    path('api/image-urls/', image_urls_view, name='image-urls'),
]