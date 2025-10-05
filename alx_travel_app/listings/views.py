from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer

class ListingViewSet(viewsets.ModelViewSet):
    """
    Manages Listing views
    """
    
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    
class BookingViewSet(viewsets.ModelViewSet):
    """
    Manages Bookings views
    """
    
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
