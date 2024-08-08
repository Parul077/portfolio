
from django.contrib import admin
from .models import ContactMessage

# Create a custom admin interface class (optional)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'message')
    search_fields = ('first_name', 'last_name', 'email')

# Register the model with the admin site
admin.site.register(ContactMessage, ContactMessageAdmin)

