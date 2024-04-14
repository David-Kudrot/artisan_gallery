from django.urls import path, include
from .views import ArtworkList
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('artowklist', ArtworkList, basename='artwork_list')


urlpatterns = [
    path('', include(router.urls)),

]
