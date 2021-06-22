from django.urls import path
from lead_auth.views.position_view import PositionAPIView

urlpatterns = [
    path('position/', PositionAPIView.as_view()),
    path('position-update/<int:pk>/', PositionAPIView.as_view()),
    path('position-delete/<int:pk>/', PositionAPIView.as_view()),
]
