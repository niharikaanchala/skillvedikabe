from django.urls import path
from .views import (
    CategoryListView,
    CategoryDetailView,
    CategoryBulkDeleteView,
    CategoryCoursesView,
    CategoryPageContentView,
)

urlpatterns = [
    path("", CategoryListView.as_view()),  # GET, POST
    path("bulk-delete/", CategoryBulkDeleteView.as_view()),  # DELETE (bulk)
    path("<int:id>/courses/", CategoryCoursesView.as_view()),  # GET
    path("<int:id>/page-content/", CategoryPageContentView.as_view()),  # GET, POST
    path("<int:id>/", CategoryDetailView.as_view()),  # GET, PUT, DELETE
]