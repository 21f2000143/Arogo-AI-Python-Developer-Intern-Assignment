from rest_framework import serializers
from clini360.models import CustomUser, MedicalRecord


class CustomUserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password", "password2", "user_type",
                  "name", "age", "gender", "address", "medical_history"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({
                "password": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop("password2")
        user = CustomUser.objects.create_user(**validated_data)
        return user


class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = ['url', 'doctor_name', 'diagnosis',
                  'prescribed_medications', 'lab_tests', 'visit_date',
                  'next_visit', 'patient']
