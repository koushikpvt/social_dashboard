# File: dashboard/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # Import views from the current module

urlpatterns = [
    # Root route
    path('', views.home_view, name='home'),  # Renders the home page

    # User Profile
    path('profile/', views.profile_view, name='profile'),  # Fetches and displays user profile data

    # API endpoints
    path('api/posts/', views.post_list_create_api, name='api-posts'),  # API for creating and listing posts
    path('api/activities/', views.activity_list_api, name='api-activities'),  # API for listing user activities

    # Authentication views
    path('login/', auth_views.LoginView.as_view(template_name='dashboard/login.html'), name='login'),  # Login page
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),  # Logout functionality
    path('signup/', views.signup, name='signup'),  # Signup page

    # Threads API authorization flow
    path('threads/auth/', views.ThreadsAuthView.as_view(), name='threads-auth'),  # Starts Threads authorization flow
    path('threads/callback/', views.ThreadsCallbackView.as_view(), name='threads-callback'),  # Handles Threads callback

    # Analytics Dashboard
    path('analytics/', views.analytics_dashboard, name='analytics_dashboard'),  # Displays analytics dashboard
]