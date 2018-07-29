from django.conf.urls import url
from .views import *
from .api import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"hotelsapi",HotelApi)
router.register(r"customersapi",CustomerApi)
router.register(r"reservationsapi",ReservationApi)
urlpatterns = router.urls




urlpatterns += [
    url(r'allhotels',AllHotels),
    url(r'allreservations',AllReservations),
    url(r'allcustomers',AllCustomers),

]
