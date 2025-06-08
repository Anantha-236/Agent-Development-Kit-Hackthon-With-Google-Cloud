from django.contrib import admin
from .models import Patient, MedicalReport, Alert
from django.contrib.auth.admin import UserAdmin

@admin.register(Patient)
class PatientAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'emergency_contact', 'medical_history', 'profile_picture')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'emergency_contact', 'medical_history', 'profile_picture')}),
    )
    list_display = ('username', 'first_name', 'last_name', 'date_of_birth', 'emergency_contact')
    search_fields = ('username', 'first_name', 'last_name', 'emergency_contact')

@admin.register(MedicalReport)
class MedicalReportAdmin(admin.ModelAdmin):
    list_display = ('patient', 'report_type', 'created_at')
    search_fields = ('patient__username', 'report_type')
    list_filter = ('report_type', 'created_at')

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('patient', 'criticality', 'created_at', 'resolved')
    search_fields = ('patient__username', 'message')
    list_filter = ('criticality', 'created_at', 'resolved')
