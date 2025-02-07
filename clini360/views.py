from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.contrib.auth import authenticate
from clini360.models import MedicalRecord
from clini360.serializers import (
    CustomUserRegistrationSerializer,
    MedicalRecordSerializer,
)
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


class RegisterUserView(APIView):
    # @csrf_exempt
    def post(self, request):
        serializer = CustomUserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                "token": token.key, "message":
                "User registered successfully"}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        # Use email for login
        user = authenticate(username=email, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                "token": token.key,
                "message": "Login successful"}, status=HTTP_200_OK)
        return Response({
            "error": "Invalid Credentials"},
            status=HTTP_400_BAD_REQUEST)


class MedicalRecordDetails(APIView):
    """
    Register a new patient, retrieve, update or delete a snippet instance.
    """

    def post(self, request, format=None):
        serializer = MedicalRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, record_id):
        try:
            return MedicalRecord.objects.get(pk=record_id)
        except MedicalRecord.DoesNotExist:
            raise Http404

    def get(self, request, record_id, format=None):
        record = self.get_object(record_id)
        serializer = MedicalRecordSerializer(record)
        return Response(serializer.data)

    def put(self, request, record_id, format=None):
        record = self.get_object(record_id)
        serializer = MedicalRecordSerializer(record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, record_id, format=None):
        record = self.get_object(record_id)
        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MedicalRecordList(APIView):
    """
    Get all the records of a patient.
    """

    def get(self, request, patient_id, format=None):
        records = MedicalRecord.objects.filter(patient=patient_id).all()
        serializer = MedicalRecordSerializer(records, many=True)
        return Response(serializer.data)
