from .models import Publication, Category, Image, Place
from rest_framework import serializers
from django.contrib.auth.models import User


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('api_url', 'name', 'description')


class PublicationSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    place = serializers.PrimaryKeyRelatedField(queryset=Place.objects.all())

    class Meta:
        model = Publication
        fields = ('api_url', 'name', 'url', 'user', 'category', 'place',
                  'latitude', 'longitude', 'altitude', 'creation_date',
                  'begin_date', 'end_date', 'description', 'active')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('api_url', 'username', 'first_name', 'last_name', 'email')


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    publication = serializers.PrimaryKeyRelatedField(queryset=Publication.objects.all())

    class Meta:
        model = Image
        fields = ('api_url', 'name', 'image', 'preview',
                  'description', 'publication')


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = ('api_url', 'name', 'description', 'latitude',
                  'longitude', 'altitude')
