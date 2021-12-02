from django.contrib import admin
from .models import User
class UserAdmin(admin.ModelAdmin):
    list_display =('email','password','username','registerd_date')

admin.site.register(User, UserAdmin)
