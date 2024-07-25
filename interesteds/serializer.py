from rest_framework import serializers
from .models import Interested

class InterestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interested
        fields = '__all__'