from rest_framework import serializers 
from .models import User, Listing

class UserSerializer(serializers.ModelSerializer):  # Converts SQL to JSON for User model
    class Meta:
        model = User
        fields = '__all__'  # Include all fields in the User model

class ListingSerializer(serializers.ModelSerializer):  # Converts SQL to JSON for Listing model
    class Meta:
        model = Listing
        fields = '__all__'  # Include all fields in the Listing model
