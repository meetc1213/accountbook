from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.contrib import admin
from signin.models import profile


# Register your models here.
class profileInline(admin.StackedInline):
    model = profile
    can_delete = False
    verbose_name_plural = 'Profiles'

class UserAdmin(BaseUserAdmin):
    inlines = (profileInline,)
admin.site.register(profile)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
