from django.urls import path
from .views import RecordingCreateView , RecordingDetaitView ,CategoryCreateView,CategoryDetaitView,FavoriteDetaitView,FavoriteCreateView,SignUpView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('recordings/', RecordingCreateView.as_view(), name='recording-create'),
    path('recordings/<int:pk>/', RecordingDetaitView.as_view(), name='recording-detail'),
    path('categories/', CategoryCreateView.as_view(), name='categories-create'),
    path('categories/<int:pk>/', CategoryDetaitView.as_view(), name='categories-detail'),
    path('favorites/', FavoriteCreateView.as_view(), name='favorites-create'),
    path('favorites/<int:pk>/', FavoriteDetaitView.as_view(), name='favorites-detail'),
    path('signup/', SignUpView.as_view(), name='signup')

]