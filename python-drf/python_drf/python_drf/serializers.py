from rest_framework.serializers import ModelSerializer, UUIDField

from python_drf.python_drf.models import Bookmark, Category


class CategorySerializer(ModelSerializer):
    id = UUIDField(read_only=False)

    class Meta:
        model = Category
        fields = ["id", "name"]


class BookmarkSerializer(ModelSerializer):
    categories = CategorySerializer(many=True)

    class Meta:
        model = Bookmark
        fields = ["id", "name", "url", "categories"]

    def create(self, validated_data):
        categories = validated_data.pop("categories")
        bookmark = Bookmark.objects.create(**validated_data)
        bookmark.categories.add(*map(lambda category: category["id"], categories))
        return bookmark
