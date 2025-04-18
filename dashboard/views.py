from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import os
from django.views import View
import pandas as pd  # For analytics dashboard
from .api import get_user_data  # Import the utility function
from .models import UserProfile


# Home view for '/'
def home_view(request):
    username = request.user.username if request.user.is_authenticated else None
    return render(request, 'dashboard/home.html', {'username': username})  # Updated template path


# Signup view
def signup(request):
    return render(request, 'dashboard/signup.html')  # Ensure correct path for the signup template


# API view for posts
@api_view(['GET', 'POST'])
def post_list_create_api(request):
    # Example response for posts API
    return Response({"message": "Post API"})


# API view for user activities
@api_view(['GET'])
def activity_list_api(request):
    # Example response for activities API
    return Response({"message": "Activity API"})


# Threads Authorization View
class ThreadsAuthView(View):
    def get(self, request):
        client_id = os.getenv("THREADS_APP_ID")
        redirect_uri = os.getenv("THREADS_REDIRECT_URI")
        scope = "threads_basic,threads_content_publish"
        state = "optional-state"

        auth_url = (
            f"https://threads.net/oauth/authorize"
            f"?client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}&response_type=code&state={state}"
        )
        return HttpResponseRedirect(auth_url)


# Threads Callback View
class ThreadsCallbackView(View):
    def get(self, request):
        code = request.GET.get('code')
        if not code:
            return JsonResponse({'error': 'Authorization code not provided'}, status=400)

        client_id = os.getenv("THREADS_APP_ID")
        client_secret = os.getenv("THREADS_APP_SECRET")
        redirect_uri = os.getenv("THREADS_REDIRECT_URI")
        token_url = "https://graph.threads.net/oauth/access_token"

        response = requests.post(token_url, data={
            'client_id': client_id,
            'client_secret': client_secret,
            'code': code,
            'grant_type': 'authorization_code',
            'redirect_uri': redirect_uri,
        })

        if response.status_code == 200:
            access_token = response.json().get('access_token')
            request.session['access_token'] = access_token  # Store access token in session
            return redirect('profile')  # Redirect to the profile page
        else:
            error_message = response.json()
            return JsonResponse({'error': error_message}, status=response.status_code)


# Profile View

def profile_view(request):
    access_token = request.session.get('access_token')
    if not access_token:
        return render(request, 'dashboard/error.html', {'message': 'Authorization required. Please log in.'})

    headers = {'Authorization': f'Bearer {access_token}'}
    api_url = f"{os.getenv('THREADS_API_BASE_URL')}/v1.0/me?fields=id,name,email,picture"

    try:
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            user_data = response.json()
            profile, created = UserProfile.objects.update_or_create(
                threads_id=user_data['id'],
                defaults={
                    'name': user_data['name'],
                    'email': user_data.get('email', ''),
                    'profile_picture': user_data.get('picture', {}).get('data', {}).get('url', '')
                }
            )
            return render(request, 'dashboard/profile.html', {'user_data': profile})
        else:
            return render(request, 'dashboard/error.html', {'message': f"API error: {response.json()}"})
    except requests.exceptions.RequestException as e:
        return render(request, 'dashboard/error.html', {'message': f"Request error: {str(e)}"})


# Analytics Dashboard View
def analytics_dashboard(request):
    # Mock data example
    data = pd.DataFrame({'Date': ['2023-01-01', '2023-01-02'], 'Users': [100, 150]})
    return render(request, 'dashboard/analytics.html', {'chart_data': data.to_dict()})