from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from accounts.models import Account
# Register your models here.


class AccountAdmin(BaseUserAdmin):
    fieldsets = [
        ("Personal Info", {"fields": ["email", 'password', 'age',
         'name', 'user_type', 'is_superuser', 'is_active', 'is_staff']}),
        ("User Permission", {'fields': ["user_permissions"]})
    ]

    add_fieldsets = [
        (None, {"fields": [
            "email", 'age', 'name', 'user_type', "password1",
            "password2",
        ]})
    ]
    list_display = ["name", "email", "user_type"]
    ordering = ['name']


# admin.site.unregister(User)
admin.site.register(Account, AccountAdmin)
