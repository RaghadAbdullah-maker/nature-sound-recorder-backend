from django.contrib import admin
from .models import Recording,Favorite,Category,Destination

# Register your models here.
admin.site.register(Recording)
admin.site.register(Category)
admin.site.register(Favorite)
admin.site.register(Destination)

