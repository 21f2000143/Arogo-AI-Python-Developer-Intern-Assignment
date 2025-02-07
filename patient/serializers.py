from rest_framework import serializers
from patient.models import MedicalRecord
from patient.models import (
    Appointment,
    User,
    PatientProfile,
    DoctorProfile,
    DoctorSlot
)


class UserSerializer(serializers.ModelSerializer):
    medical_reports = serializers.PrimaryKeyRelatedField(
        many=True, queryset=MedicalRecord.objects.all())

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'name',
                  'age', 'gender', 'contact', 'role', 'medical_reports']


class PatientRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    medical_history = serializers.JSONField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'name',
                  'age', 'gender', 'contact', 'medical_history']

    def create(self, validated_data):
        medical_history = validated_data.pop('medical_history', {})
        user = User.objects.create_user(
            role='patient', **validated_data
        )
        PatientProfile.objects.create(
            user=user, medical_history=medical_history)
        return user


class DoctorRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    specialization = serializers.CharField(required=True)
    experience = serializers.IntegerField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'name', 'age',
                  'gender', 'contact', 'specialization', 'experience']

    def create(self, validated_data):
        specialization = validated_data.pop('specialization')
        experience = validated_data.pop('experience')
        user = User.objects.create_user(
            role='doctor', **validated_data
        )
        DoctorProfile.objects.create(
            user=user, specialization=specialization, experience=experience)
        return user


class MedicalRecordSerializer(serializers.ModelSerializer):
    patient = serializers.ReadOnlyField(source='patient.username')

    class Meta:
        model = MedicalRecord
        fields = ['id', 'doctor_name', 'diagnosis',
                  'prescribed_medications', 'lab_tests', 'visit_date',
                  'next_visit', 'patient']


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class DoctorSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorSlot
        fields = '__all__'
