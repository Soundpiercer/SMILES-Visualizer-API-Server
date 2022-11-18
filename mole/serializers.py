from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Molecular


class MolecularSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Molecular
        fields = ["owner", "id", "formula", "effect", "others"]


class UserSerializer(serializers.ModelSerializer):
    moleculars = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Molecular.objects.all()
    )

    class Meta:
        model = User
        field = ["id", "username", "moleculars"]
