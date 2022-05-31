from django.urls import path
from .views import BikeList, BikeDetail

urlpatterns = [
  path('', BikeList.as_view(), name='bike_list'),
  path('<int:pk>/', BikeDetail.as_view(), name='bike_detail')
]