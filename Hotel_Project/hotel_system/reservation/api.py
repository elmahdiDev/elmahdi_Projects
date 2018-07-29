from rest_framework.viewsets import ModelViewSet
from .serializer import *
from .models import *

class HotelApi(ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class CustomerApi(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ReservationApi(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer