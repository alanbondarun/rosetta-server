from rest_framework.serializers import ModelSerializer

from python_drf.python_drf.models import Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]
