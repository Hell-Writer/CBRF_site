from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from companies.models import Organisation


class OrganisationSerializer(serializers.ModelSerializer):
    organisation_type = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        fields = ("__all__")
        model = Organisation