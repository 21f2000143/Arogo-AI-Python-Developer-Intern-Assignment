from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.


# Customizing the user model
class User(AbstractUser):
    USER_TYPES = [
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
    ]
    role = models.CharField(max_length=10, choices=USER_TYPES)
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(
        max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')]
    )
    contact = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.username} ({self.role})"


class PatientProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="patient_profile")
    medical_history = models.JSONField(default=dict)


class DoctorProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="doctor_profile")
    specialization = models.CharField(max_length=255)
    experience = models.PositiveIntegerField()


class MedicalRecord(models.Model):
    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="medical_reports")
    doctor_name = models.CharField(max_length=255)
    diagnosis = models.TextField()
    prescribed_medications = models.JSONField()  # Stores a list of medicines
    lab_tests = models.JSONField()  # Stores a list of tests conducted
    visit_date = models.DateTimeField(auto_now_add=True)
    next_visit = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Report for {self.doctor_name} on {self.visit_date.date()}"


class DoctorSlot(models.Model):
    doctor = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="slots")
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_booked = models.BooleanField(default=False)

    class Meta:
        unique_together = ['doctor', 'date',
                           'start_time']  # Avoid duplicate slots

    def __str__(self):
        return f"{self.doctor.name} - {self.date} ({self.start_time} - {self.end_time})"


class Appointment(models.Model):
    STATUS_CHOICES = [
        ('booked', 'Booked'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('rescheduled', 'Rescheduled'),
    ]

    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="patient_appointments")
    doctor = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="doctor_appointments")
    slot = models.ForeignKey(
        DoctorSlot, on_delete=models.CASCADE, related_name="appointments")
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="booked")
    booked_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Appointment: {self.patient.name} with {self.doctor.name} on {self.availability.date}"


class Notification(models.Model):
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notifications")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.recipient.username} - Read: {self.is_read}"
