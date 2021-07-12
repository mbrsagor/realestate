from django.urls import path
from inventory.views.category_view import CategoryAPIView

urlpatterns = [
    # Category API endpoint
    path('category/', CategoryAPIView.as_view(), name='category_list'),
    path('category/create/', CategoryAPIView.as_view(), name='category_create'),
    path('category/update/<pk>/', CategoryAPIView.as_view(), name='category_update'),
    path('category/delete/<pk>/', CategoryAPIView.as_view(), name='category_delete'),
]
