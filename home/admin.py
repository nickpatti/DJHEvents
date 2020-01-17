from django.contrib import admin
from .models import EventType, HomePage, ContactPost

# Register your models here.
admin.site.register(ContactPost)
admin.site.register(EventType)
admin.site.register(HomePage)
