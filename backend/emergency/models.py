from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class EmergencyContact(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='emergency_contacts')
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    relationship = models.CharField(max_length=50)
    is_primary = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_primary', 'name']

    def __str__(self):
        return f"{self.name} ({self.relationship})"

class EmergencyAlert(models.Model):
    class AlertStatus(models.TextChoices):
        PENDING = 'PENDING', _('Pending')
        ACTIVE = 'ACTIVE', _('Active')
        RESOLVED = 'RESOLVED', _('Resolved')
        CANCELLED = 'CANCELLED', _('Cancelled')

    class AlertType(models.TextChoices):
        MEDICAL = 'MEDICAL', _('Medical Emergency')
        MENTAL_HEALTH = 'MENTAL_HEALTH', _('Mental Health Crisis')
        SAFETY = 'SAFETY', _('Safety Concern')
        OTHER = 'OTHER', _('Other Emergency')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='emergency_alerts')
    alert_type = models.CharField(max_length=20, choices=AlertType.choices)
    status = models.CharField(
        max_length=10,
        choices=AlertStatus.choices,
        default=AlertStatus.PENDING
    )
    description = models.TextField()
    location = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.alert_type} Alert - {self.status}"

class EmergencyResponse(models.Model):
    alert = models.ForeignKey(EmergencyAlert, on_delete=models.CASCADE, related_name='responses')
    responder = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    action_taken = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Response to {self.alert.alert_type} Alert at {self.created_at}"
