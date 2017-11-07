from rest_framework import serializers
from .models import Farms

class FarmsSerializer(serializers.ModelSerializer):

    class Meta:

        model = Farms
        fields = '__all__'