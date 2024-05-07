from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from apps.models import User, Product


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = 'user_image', 'first_name', 'last_name', 'is_staff'
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", 'avatar')}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", 'avatar', "password1", "password2"),
            },
        ),
    )

    def user_image(self, obj: User):
        return format_html(
            f'<a href="{obj.pk}">'
            f'<img src="{obj.avatar.url}" width="35" height="35" style="object-fit: cover; border-radius: 50%"></a>'
        )

    user_image.short_description = 'Image'


@admin.register(Product)
class ProductModelAdmin(ModelAdmin):
    pass


admin.site.unregister(Group)
