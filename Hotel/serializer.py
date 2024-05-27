from rest_framework import serializers
from .models import Hotel , City, Features, HotelImages, Stay, StayImages, HotelComments




class HotelSerializer(serializers.ModelSerializer):
    main_image = serializers.ImageField(max_length=None , use_url=True)

    class Meta:
        model = Hotel
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None , use_url=True)

    class Meta:
        model = City
        fields = '__all__'

class HotelFeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        fields = '__all__'

class HotelImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImages
        fields = '__all__'


class StayImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StayImages
        fields = '__all__'


class StaySerializer(serializers.ModelSerializer):
    stay_images = StayImagesSerializer(many=True, read_only=True)
    class Meta:
        model = Stay 
        fields = ['hotel_id', 'stay_type', 'price', 'description', 'stay_images']



class HotelCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelComments 
        fields = '__all__'


class HotelBigSerializer(serializers.ModelSerializer):
    hotel_images = HotelImagesSerializer(many=True, read_only=True)
    features = HotelFeaturesSerializer(many=True, read_only=True)
    stays = StaySerializer(many=True, read_only=True)
    comments = HotelCommentsSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = ['name', 'email', 'phone', 'country', 'city', 'main_image', 'date_created', 'sum_of_rates', 'number_of_rates', 'hotel_images', 'features', 'stays', 'stays_images', 'comments']