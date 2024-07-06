"""
Serializers for the recipe API.
"""

from core.models import Recipe
from rest_framework import serializers


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipes."""

    class Meta:
        model = Recipe
        fields = [
            'id',
            'title',
            'time_minutes', 'price',
            'link'
        ]
        read_only_fields = ['id']
