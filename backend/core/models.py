from django.db import models
from django.contrib.auth.models import AbstractUser

class Patient(AbstractUser):
    date_of_birth = models.DateField()
    emergency_contact = models.CharField(max_length=20)
    medical_history = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class MedicalReport(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    report_type = models.CharField(max_length=100)  # e.g., X-Ray, Blood Test
    report_file = models.FileField(upload_to='reports/')
    created_at = models.DateTimeField(auto_now_add=True)
    analysis_results = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"{self.report_type} for {self.patient}"

class Alert(models.Model):
    CRITICALITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    message = models.TextField()
    criticality = models.CharField(max_length=10, choices=CRITICALITY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.criticality} alert for {self.patient}"
