from django.urls import path
from .views import BlogListView, BlogDetailView, BlogBulkDeleteView, MetaTagsAPI, MetaTagsDetailAPI

urlpatterns = [
    path('meta-tags/', MetaTagsAPI.as_view(), name='meta-tags'),
    path('meta-tags/<int:pk>/', MetaTagsDetailAPI.as_view(), name='meta-tags-detail'),
    path('delete-multiple/', BlogBulkDeleteView.as_view(), name='blog-bulk-delete'),
    path('', BlogListView.as_view(), name='blog-list'),
    path('<slug:slug>/', BlogDetailView.as_view(), name='blog-detail'),
]