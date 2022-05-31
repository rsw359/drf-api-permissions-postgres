from rest_framework import generics
from .models import Bike
from .serializers import BikeSerializer
from .permissions import IsOwnerOrReadOnly

class BikeList(generics.ListCreateAPIView):
  queryset = Bike.objects.all()
  serializer_class = BikeSerializer

class BikeDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  queryset = Bike.objects.all()
  serializer_class = BikeSerializer
