from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from account.models import User

# UserAdmin.fieldsets += (
#     ("custom fields", {"fields": ("is_author", "special_user")})
# )
# or add custom fields to personal info section

UserAdmin.fieldsets[2][1]['fields'] = (
    "is_active",
    "is_staff",
    "is_superuser",
    "is_author",
    "special_user",
    "groups",
    "user_permissions",

)

UserAdmin.list_display += ("is_author", "is_special_user")
admin.site.register(User, UserAdmin)
