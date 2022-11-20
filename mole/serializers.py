from rest_framework import serializers
from .models import Molecular


class MolecularSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Molecular
        fields = ["owner", "id", "formula", "effect", "others"]
