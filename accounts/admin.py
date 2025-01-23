from django.contrib import admin

from accounts.models import User, Profile
from django.contrib.auth.admin import UserAdmin 

# Custom User Admin Panel
class UserAdminPanel(UserAdmin):
    list_display = ("email", "is_active","is_staff", "is_superuser")
    list_filter = ("email",)
    search_fields = ("email",)
    ordering = ("-email",)
    
    fieldsets = (
        ("Authentication", {
           "fields": ("email", "password"), 
        }),
        ("Permissions", {
           "fields": ("is_active", "is_staff", "is_superuser"), 
        }),
        ("Groups Permissions", {
           "fields": ("groups", "user_permissions"), 
        }),
        ("Important Dates", {
           "fields": ("last_login",), 
        }),
    )
    
    add_fieldsets = (
        ("Authentication",{
            "classes" : ("wide",),
            "fields" : ("email", "password1", "password2", "is_active", "is_staff" ,"is_superuser"),
        }),
    )
    
# Profile Admin Panel
class ProfileAdminPanel(admin.ModelAdmin):
    list_display = ("user", "first_name", "last_name", "created_date")
    list_filter = ("user", "first_name", "last_name")
    search_fields = ("first_name", "last_name")
    ordering = ("-created_date", )

admin.site.register(User, UserAdminPanel)
admin.site.register(Profile, ProfileAdminPanel)