from django.urls import path, include
from .views import CompanyViewSet, CityViewSet, RegionViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'company', CompanyViewSet, basename='company')
router.register(r'city', CityViewSet, basename='city')
router.register(r'region', RegionViewSet, basename='region')

urlpatterns = [
    path('', include(router.urls)),
]