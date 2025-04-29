from rest_framework import generics
from django.views import View
from django.http import HttpResponse
from .serializers import UserSerializer, ListingSerializer
from .models import User, Listing

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = UserSerializer # tell django what serializer to use

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

class ListingList(generics.ListCreateAPIView):
    queryset = Listing.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = ListingSerializer # tell django what serializer to use

class ListingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all().order_by('id')
    serializer_class = ListingSerializer

class HomePageView(View):
    def get(self, request):
        return HttpResponse("Welcome to the home page!")