from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet, RegisterView
from rest_framework.authtoken import views as authviews

router = DefaultRouter()
router.register(r'notes', NoteViewSet, basename='note')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', authviews.obtain_auth_token, name='login'),
]
