from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from profiles_api_app import views


# ===================USE THE BELOW FOR ViewSets

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)



# =================USE THE BELOW FOR APIViewSet  =====================

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]