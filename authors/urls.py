from django.urls import path, include
from .views import AuthorViewSet
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers



router = routers.DefaultRouter()
router.register('authors', AuthorViewSet)

urlpatterns = [
   
    path('', include(router.urls)),
    
]