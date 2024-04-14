from rest_framework import serializers
from .models import Category, Artwork

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class ArtworkSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(many=False,source='owner.name', read_only=True)
    category = serializers.StringRelatedField(many=False)
    class Meta:
        model = Artwork
        fields = ['id', 'owner', 'title', 'image', 'description', 'category', 'created_at']
