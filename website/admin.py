from django.contrib import admin
from website.models import ContactForm, PhotoSample

# Contact admin panel
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_date")
    list_filter = ("email", "subject")
    search_fields = ("email", "subject")
    ordering = ("-created_date",)
    
# PhotoSample admin panel
class PhotoSampleAdminPanel(admin.ModelAdmin):
    list_display = ("title", "status" ,"created_date")
    list_filter = ("title",)
    search_fields = ("title",)
    ordering = ("-created_date", )
    
admin.site.register(ContactForm, ContactAdmin)
admin.site.register(PhotoSample, PhotoSampleAdminPanel)
