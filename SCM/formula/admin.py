from django.contrib import admin
from .models import Registration

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ( 'Application_number','last_name', 'first_name')
    def has_change_permission(self, request, obj=None):
          return False
admin.site.register(Registration, RegistrationAdmin)

