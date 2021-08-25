from django.urls import path, include
from .views import BookViewSet ,searchBook
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers



router = routers.DefaultRouter()
router.register('books', BookViewSet)

urlpatterns = [
   
    path('', include(router.urls)),
    path('books/search-book', searchBook)
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)