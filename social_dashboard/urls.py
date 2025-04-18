# File: social_dashboard/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin route
    path('', include('dashboard.urls')),  # Includes routes from the dashboard app
]