from rest_framework import generics
from django.views import View
from django.http import HttpResponse
from rest_framework.exceptions import ValidationError
from .serializers import UserSerializer, ListingSerializer
from django.contrib.auth.hashers import make_password
from .models import User, Listing

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = UserSerializer # tell django what serializer to use

    # def perform_create(self, serializer):
    #     name = serializer.validated_data.get('name')

    #     if User.objects.filter(name=name).exists():
    #         raise ValidationError("A user with this name already exists.")
        


class UserLogin(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().order_by('id')

    # def login(request, username):
    #     test = User(username, )
    #     return test

class ListingList(generics.ListCreateAPIView):
    queryset = Listing.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = ListingSerializer # tell django what serializer to use

class ListingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all().order_by('id')
    serializer_class = ListingSerializer

class HomePageView(View):
    def get(self, request):
        return HttpResponse("Welcome to the home page!")