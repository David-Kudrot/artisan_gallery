from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from artwork.models import Artwork, Category
from artwork.serializers import ArtworkSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets


# class ArtworkList(viewsets.ModelViewSet):
#     # permission_classes = [IsAuthenticated]
#     def get(self, request):
#         artworks = Artwork.objects.all()
#         serializer = ArtworkSerializer(artworks, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         permission_classes = [IsAuthenticated]  # Require authentication for POST
#         permission_instance = [permission() for permission in permission_classes]
#         self.check_permissions(request)
#         # Extract data from request
#         artwork_data = request.data.get('artwork', {})
#         category_data = artwork_data.pop('category', None)

#         # Create or retrieve category
#         if category_data:
#             category_serializer = CategorySerializer(data=category_data)
#             if category_serializer.is_valid():
#                 category = category_serializer.save()
#             else:
#                 return Response(category_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             category = None

#         # Create artwork
#         artwork_serializer = ArtworkSerializer(data=artwork_data)
#         if artwork_serializer.is_valid():
#             artwork_serializer.save(category=category)  # Assign category to artwork
#             return Response(artwork_serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(artwork_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        







class ArtworkList(viewsets.ModelViewSet):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
    # permission_classes = [IsAuthenticated]  # Require authentication for all actions

    def perform_create(self, serializer):
        category_data = self.request.data.get('category', None)
        category = None
        if category_data:
            category_serializer = CategorySerializer(data=category_data)
            if category_serializer.is_valid():
                category = category_serializer.save()
        
        serializer.save(category=category)

