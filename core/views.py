from .models import Publication, Category
from rest_framework import viewsets
from .serializers import PublicationSerializer, CategorySerializer, UserSerializer
from django.contrib.auth.models import User


class PublicationViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
