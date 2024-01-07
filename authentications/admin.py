from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from authentications import models as authentication_models


class CustomUserAdmin(UserAdmin):
    """
    User admin class for User model
    """
    fieldsets = (
        UserAdmin.fieldsets +
        (
            (
                _('Additional fields'),
                {'fields': ('login_count', )}
            ),
        )
    )


admin.site.register(authentication_models.User, CustomUserAdmin)
