from .models import Publication, Category, Place, Image
from rest_framework import viewsets, filters, generics
from .serializers import PublicationSerializer, CategorySerializer, UserSerializer, PlaceSerializer, ImageSerializer
from django.contrib.auth.models import User
from .permissions import CsrfExemptSessionAutentication


class PublicationViewSet(viewsets.ModelViewSet):
    """
    """
    authentication_classes = (CsrfExemptSessionAutentication,)
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    """
    authentication_classes = (CsrfExemptSessionAutentication,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PlaceViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class ImageViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class PublicationHomeView(generics.ListAPIView):
    """
    """
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend, filters.OrderingFilter,)
    search_fields = ('name', 'description')
    filter_fields = ('category', 'place')
    ordering_fields = ('begin_date', 'name')
