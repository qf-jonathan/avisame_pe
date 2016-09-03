from rest_framework import routers
from django.conf.urls import url, include
from core import views

router = routers.DefaultRouter()
router.register(r'publication', views.PublicationViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'user', views.UserViewSet)
router.register(r'image', views.ImageViewSet)
router.register(r'place', views.PlaceViewSet)

urlpatterns = [
    url(r'^publication_home/$', views.PublicationHomeView.as_view()),
    url(r'^', include(router.urls)),
]
