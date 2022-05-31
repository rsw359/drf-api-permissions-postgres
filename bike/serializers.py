from rest_framework import serializers
from .models import Bike

class BikeSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('id', 'name', 'color', 'description', 'purchaser', 'created_at')
    model = Bike