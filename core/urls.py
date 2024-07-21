from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, EventView, ClubView, AttendanceView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('events/', EventView.as_view(), name='events'),
    path('clubs/', ClubView.as_view(), name='clubs'),
    path('attendance/', AttendanceView.as_view(), name='attendance'),
]