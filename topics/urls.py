from django.urls import path, include
from .views import TopicViewSet
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers



router = routers.DefaultRouter()
router.register('topics', TopicViewSet)

urlpatterns = [
   
    path('', include(router.urls)),
    
]