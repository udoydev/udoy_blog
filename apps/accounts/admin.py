from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import user




@admin.register(user)
class CustomUserAdmin(UserAdmin):
    model = user

    list_display = (
        'id',
        'email',
        'username',
        'full_name',
        'role',
        'is_staff',
        'is_superuser',
    )

    list_filter = (
        'role',
        'is_staff',
        'is_superuser',
        'is_active',
    )

    ordering = ('email',)

    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {
            'fields': ('full_name', 'phone', 'role'),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Fields', {
            'fields': ('full_name', 'phone', 'role'),
        }),
    )
