from rest_framework.serializers import (
    ModelSerializer,
)

from python_drf.python_drf.models import Bookmark, Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class BookmarkSerializer(ModelSerializer):
    categories = CategorySerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Bookmark
        fields = ["id", "name", "url", "categories"]
