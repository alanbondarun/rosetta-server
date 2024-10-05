from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from python_drf.python_drf.models import Category
from python_drf.python_drf.serializers import CategorySerializer


class CategoryList(APIView):
    def get(self, request: Request):
        categories = Category.objects.all()
        if request.query_params and request.query_params["name"]:
            categories = filter(
                lambda category: request.query_params["name"].lower()
                in category.name.lower(),
                categories,
            )
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
