from uuid import uuid4

from django.db.models import ObjectDoesNotExist
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from python_drf.python_drf.models import Bookmark, Category
from python_drf.python_drf.serializers import BookmarkSerializer, CategorySerializer


class CategoryList(APIView):
    def get(self, request: Request):
        categories = Category.objects.all()
        if request.query_params and request.query_params["name"]:
            categories = filter(
                lambda category: str(request.query_params["name"]).lower()
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


class CategoryDelete(APIView):
    def delete(self, request: Request, id: str):
        try:
            category = Category.objects.get(pk=id)
            category.delete()
            return Response({"isDeleted": True})
        except ObjectDoesNotExist:
            return Response({"isDeleted": False})


class BookmarkList(APIView):
    def get(self, request: Request):
        bookmarks = Bookmark.objects.all()
        if request.query_params and request.query_params["categoryId"]:
            bookmarks = filter(
                lambda bookmark: any(
                    str(category.id) == request.query_params["categoryId"]
                    for category in bookmark.categories.all()
                ),
                bookmarks,
            )
        serializer = BookmarkSerializer(bookmarks, many=True)
        return Response(serializer.data)

    def post(self, request: Request):
        categories = list(
            map(
                lambda category_id: {
                    "id": category_id,
                    "name": Category.objects.get(pk=category_id).name,
                },
                request.data["categoryIds"],
            )
        )
        serializer = BookmarkSerializer(
            data={
                **request.data,
                "id": str(uuid4()),
                "categories": categories,
            }
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookmarkDelete(APIView):
    def delete(self, request: Request, id: str):
        try:
            category = Bookmark.objects.get(pk=id)
            category.delete()
            return Response({"isDeleted": True})
        except ObjectDoesNotExist:
            return Response({"isDeleted": False})
