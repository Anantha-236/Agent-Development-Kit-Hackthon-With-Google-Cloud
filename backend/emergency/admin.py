from django.contrib import admin
from .models import EmergencyContact, EmergencyAlert, EmergencyResponse

@admin.register(EmergencyContact)
class EmergencyContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'phone_number', 'relationship', 'is_primary')
    search_fields = ('name', 'user__username', 'phone_number')
    list_filter = ('is_primary', 'relationship')

@admin.register(EmergencyAlert)
class EmergencyAlertAdmin(admin.ModelAdmin):
    list_display = ('alert_type', 'user', 'status', 'created_at', 'resolved_at')
    search_fields = ('user__username', 'description', 'location')
    list_filter = ('alert_type', 'status', 'created_at')

@admin.register(EmergencyResponse)
class EmergencyResponseAdmin(admin.ModelAdmin):
    list_display = ('alert', 'responder', 'created_at')
    search_fields = ('alert__user__username', 'responder__username', 'action_taken')
    list_filter = ('created_at',)

# Register your models here.
