from rest_framework import serializers
from ...models import Phase

class PhaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phase
        fields = ['id', 'name']  # Adjust fields as necessary