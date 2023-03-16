from django.contrib import admin
from .models import Photo, User, UserTier
from django.contrib.auth.admin import UserAdmin


# Register your models here.
admin.site.register(Photo)
admin.site.register(UserTier)
admin.site.register(User, UserAdmin)
