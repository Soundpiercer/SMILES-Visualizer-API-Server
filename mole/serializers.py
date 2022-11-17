from rest_framework import serializers
from .models import Molecular

class MolecularSerializer(serializers.ModelSerializer):
    class Meta:
        model = Molecular
        fields = ['id', 'formula', 'effect', 'others']