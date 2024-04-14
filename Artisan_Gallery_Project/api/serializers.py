from rest_framework import serializers
from artwork.models import Category, Artwork
from artist.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class ArtworkSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.name', read_only=True)
    category = serializers.StringRelatedField(many=False)

    class Meta:
        model = Artwork
        fields = ['id', 'user_name', 'title', 'image', 'description', 'category', 'created_at']

    def create(self, validated_data):
        user = self.context['request'].user
        artwork = Artwork.objects.create(user=user, **validated_data)
        return artwork