from .views import PositionAPIView
from django.urls import path

urlpatterns = [
    path('position/', PositionAPIView.as_view()),
    path('position-update/<int:pk>/', PositionAPIView.as_view()),
    path('position-delete/<int:pk>/', PositionAPIView.as_view()),
]
