from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS, BasePermission
from .models import Artwork, Category
from .serializers import ArtworkSerializer, CategorySerializer

class ReadOnlyOrIsAuthenticated(BasePermission):
    """
    Custom permission to allow read-only access to everyone,
    but only authenticated users can perform write operations.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True  # Allow any GET request.
        return request.user and request.user.is_authenticated

class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to allow owners of an object to edit or delete it,
    but restricts other users to read-only access.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.owner == request.user

class ArtworkListView(viewsets.ModelViewSet):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
    permission_classes = [ReadOnlyOrIsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        category_name = self.request.data.get('category', None)
        category = None
        if category_name:
            # Check if the category already exists
            category_instance = Category.objects.filter(name=category_name).first()
            if category_instance:
                category = category_instance
            else:
                # If category doesn't exist, create it
                category_serializer = CategorySerializer(data={'name': category_name})
                if category_serializer.is_valid():
                    category = category_serializer.save()

        serializer.save(category=category, owner=self.request.user)
