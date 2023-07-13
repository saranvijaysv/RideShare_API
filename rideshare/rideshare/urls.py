"""
URL configuration for rideshare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from rideshare_app.views import *


router = routers.DefaultRouter()
router.register('users', UserViewSet,basename='user')
router.register('login',LoginViewSet,basename='login')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('rides/', RideListView.as_view(), name='ride-list'),
    path('rides/create/', RideCreateView.as_view(), name='ride-create'),
    path('rides/<int:pk>/', RideDetailView.as_view(), name='ride-detail'),
    path('status/<int:pk>/', RideStatusUpdateAPIView.as_view(), name='ride-status-update'),
    path('match/', MatchRideView.as_view(), name='ride-match'),
    path('accept/<int:pk>/', AcceptRideView.as_view(), name='ride-accept'),
]
