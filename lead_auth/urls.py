from django.urls import path
from lead_auth.views.position_view import PositionAPIView
from lead_auth.views.user_category_view import UserCategoryAPIView

urlpatterns = [
    path('position/', PositionAPIView.as_view()),
    path('position-update/<int:pk>/', PositionAPIView.as_view()),
    path('position-delete/<int:pk>/', PositionAPIView.as_view()),
    # User category
    path('user-category/', UserCategoryAPIView.as_view()),
]
