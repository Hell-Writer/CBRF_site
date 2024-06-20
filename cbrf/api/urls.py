from django.urls import path, include
from .views import CompanyViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'company', CompanyViewSet, basename='company')

urlpatterns = [
    path('', include(router.urls)),
]