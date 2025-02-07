from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


# class CustomUser(AbstractUser):
#     USER_TYPES = (("doctor", "Doctor"), ("patient", "Patient"))

#     email = models.EmailField(unique=True)
#     user_type = models.CharField(max_length=10, choices=USER_TYPES)
#     name = models.CharField(max_length=255)
#     age = models.IntegerField()
#     gender = models.CharField(max_length=255)
#     address = models.TextField()
#     medical_history = models.JSONField()

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = ["username"]

#     def __str__(self):
#         return f"{self.username} - {self.user_type}"

class User(AbstractUser):
    pass


class MedicalRecord(models.Model):
    patient = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="medical_reports")
    doctor_name = models.CharField(max_length=255)
    diagnosis = models.TextField()
    prescribed_medications = models.JSONField()  # Stores a list of medicines
    lab_tests = models.JSONField()  # Stores a list of tests conducted
    visit_date = models.DateTimeField(auto_now_add=True)
    next_visit = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Report for {self.patient.name} on {self.visit_date.date()}"
