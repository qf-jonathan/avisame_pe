from django.contrib import admin
from .models import Publication, Category, Place, Image

admin.site.register(Category)
admin.site.register(Publication)
admin.site.register(Place)
admin.site.register(Image)
