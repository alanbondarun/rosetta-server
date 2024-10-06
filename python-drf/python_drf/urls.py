from django.urls import path

from python_drf.python_drf import views

urlpatterns = [
    path("category/", views.CategoryList.as_view()),
    path("category/<str:id>/", views.CategoryDelete.as_view()),
    path("bookmark/", views.BookmarkList.as_view()),
    path("bookmark/<str:id>/", views.BookmarkDelete.as_view()),
]
