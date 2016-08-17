from rest_framework import routers
from core import views

router = routers.DefaultRouter()
router.register(r'publication', views.PublicationViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'user', views.UserViewSet)
