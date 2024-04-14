from django.urls import path, include
from rest_framework.routers import DefaultRouter
from artwork.views import ArtworkListView


router = DefaultRouter()
router.register('artworks', ArtworkListView, basename='artwork-list')


urlpatterns = [
    path('', include(router.urls)),
]

