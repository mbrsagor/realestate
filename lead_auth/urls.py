from .views import PositionAPIView
from django.urls import path

urlpatterns = [
    path('position/', PositionAPIView.as_view()),
]
