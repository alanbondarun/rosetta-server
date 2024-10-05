from uuid import uuid4

from rest_framework import status
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

    def post(self, request: Request):
        serializer = CategorySerializer(data={**request.data, "id": str(uuid4())})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
