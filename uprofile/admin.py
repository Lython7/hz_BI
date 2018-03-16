from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Uprofile

# Register your models here.
class UprofileInline(admin.StackedInline):
    model = Uprofile
    can_delete = False
    fk_name = 'user'
    max_num = 1

class UserAdmin(BaseUserAdmin):
    inlines = [UprofileInline, ]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Uprofile)