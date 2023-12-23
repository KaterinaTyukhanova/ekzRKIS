from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Tovar, User


admin.site.register(Tovar)
admin.site.register(User, UserAdmin)


