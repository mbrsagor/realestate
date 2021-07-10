from django.urls import path
from inventory.views.category_view import CategoryAPIView

urlpatterns = [
    path('category', CategoryAPIView.as_view(), name='category_list'),
]
