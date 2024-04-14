from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Artwork, Category
from .serializers import ArtworkSerializer, CategorySerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS

class ReadOnlyOrIsAuthenticated(BasePermission):
    """
    Custom permission to allow read-only access to everyone,
    but only authenticated users can perform write operations.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True  # Allow any GET request.
        return request.user and request.user.is_authenticated

class ArtworkListView(viewsets.ModelViewSet):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
    permission_classes = [ReadOnlyOrIsAuthenticated]
    def perform_create(self, serializer):
        category_data = self.request.data.get('category', None)
        category = None
        if category_data:
            category_serializer = CategorySerializer(data=category_data)
            if category_serializer.is_valid():
                category = category_serializer.save()
        
        serializer.save(category=category)