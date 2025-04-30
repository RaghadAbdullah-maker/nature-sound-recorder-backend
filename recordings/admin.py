from django.contrib import admin
from .models import Recording,Favorite,Category

# Register your models here.
admin.site.register(Recording)
admin.site.register(Category)
admin.site.register(Favorite)
