from rest_framework import serializers
from .models import *

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        exclude = []

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        exclude = []

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        exclude = []