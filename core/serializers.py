from .models import Publication, Category
from rest_framework import serializers
from django.contrib.auth.models import User


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'description')


class PublicationSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.StringRelatedField()
    category = CategorySerializer()

    class Meta:
        model = Publication
        fields = ('name', 'url', 'user', 'category',
                  'latitude', 'longitude', 'altitude',
                  'creation_date', 'begin_date', 'end_date',
                  'description', 'active')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
