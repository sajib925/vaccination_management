from django.urls import path
from .views import BookingList, BookingDetail

urlpatterns = [
    path('', BookingList.as_view(), name='booking-list'),
    path('<int:pk>/', BookingDetail.as_view(), name='booking-detail'),
]
