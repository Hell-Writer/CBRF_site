from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from companies.models import Organisation, City, Region


class OrganisationSerializer(serializers.ModelSerializer):
    organisation_type = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        fields = ("__all__")
        model = Organisation


class CitySerializer(serializers.ModelSerializer):
    region = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        fields = ("__all__")
        model = City


class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ("__all__")
        model = Region