from django.urls import path
from inventory.views.category_view import CategoryAPIView
from inventory.views.inventory_views import InventoryAPIView

urlpatterns = [
    # Category API endpoint
    path('category/', CategoryAPIView.as_view(), name='category_list'),
    path('category/create/', CategoryAPIView.as_view(), name='category_create'),
    path('category/update/<pk>/', CategoryAPIView.as_view(), name='category_update'),
    path('category/delete/<pk>/', CategoryAPIView.as_view(), name='category_delete'),
    # Inventory API endpoint
    path('inventory/', InventoryAPIView.as_view(), name='inventory_create_list'),

]
