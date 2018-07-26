from rest_framework.generics import ListAPIView
from .serializer import HotelSerializer
from .models import Hotel

class HotelApi(ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer