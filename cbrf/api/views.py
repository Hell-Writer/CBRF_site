from django.shortcuts import get_object_or_404
from companies.models import Organisation, City, Region
from companies.serializers import OrganisationSerializer, CitySerializer, RegionSerializer
from rest_framework import (filters, generics, mixins, permissions, status,
                            viewsets)


class CompanyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer
    lookup_field = 'name_short'
    filter_backends = [filters.SearchFilter]
    search_fields = ('name_short', 'inn', 'ogrn')


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    lookup_field = 'name'
    filter_backends = [filters.SearchFilter]
    search_fields = ('name', 'id')


class RegionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    lookup_field = 'name'
    filter_backends = [filters.SearchFilter]
    search_fields = ('name','id')
