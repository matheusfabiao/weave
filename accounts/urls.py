from django.urls import path

from .views import (
    ProfileDetailView,
    ProfileUpdateView,
    RegisterView,
    UserLoginView,
    UserLogoutView,
)

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path(
        'profile/<int:pk>/', ProfileDetailView.as_view(), name='profile_detail'
    ),
    path(
        'profile/<int:pk>/update/',
        ProfileUpdateView.as_view(),
        name='profile_update',
    ),
]
