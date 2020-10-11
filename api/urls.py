from django.urls import path, include
from .views import *
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# API Router #
router = routers.DefaultRouter()

router.register(prefix='users', viewset=UserView, basename='users')
router.register(prefix='tasks', viewset=TaskView, basename='tasks')
router.register(prefix='board_column', viewset=BoardColumnView, basename='board_column')
router.register(prefix='project', viewset=ProjectView, basename='project')

urlpatterns = [
    path('', include(router.urls), name='api'),
]
