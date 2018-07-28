from rest_framework.viewsets import ModelViewSet
from .serializer import HotelSerializer
from .models import Hotel

class HotelApi(ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer