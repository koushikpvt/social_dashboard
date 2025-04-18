from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, UserActivityViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'activities', UserActivityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
