from django.urls import path, include
from .views import StorageViewSet
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers



router = routers.DefaultRouter()
router.register('storages', StorageViewSet)

urlpatterns = [
   
    path('', include(router.urls)),
    
]