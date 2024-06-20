from django.shortcuts import get_object_or_404
from companies.models import Organisation
from companies.serializers import OrganisationSerializer
from rest_framework import (filters, generics, mixins, permissions, status,
                            viewsets)


class CompanyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer
    lookup_field = 'name_short'
    filter_backends = [filters.SearchFilter]
    search_fields = ('name_short', 'inn', 'ogrn')

