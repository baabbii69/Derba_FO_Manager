from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'trailers', TrailerViewSet)
router.register(r'drivers', DriverViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
