from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'allhotels',AllHotels),
    url(r'allreservations',AllReservations),
    url(r'allcustomers',AllCustomers),

]
