from patient.permissions import IsOwnerOrReadOnly
from rest_framework import permissions
from rest_framework import generics
from patient.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from patient.models import (
    MedicalRecord,
    Appointment,
    DoctorSlot
)
from patient.serializers import (
    MedicalRecordSerializer,
    UserSerializer,
    PatientRegisterSerializer,
    DoctorRegisterSerializer,
    AppointmentSerializer,
    DoctorSlotSerializer
)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'records': reverse('record-list', request=request, format=format),
        'appointments': reverse('appointment-list', request=request, format=format),
        'slots': reverse('slot-list', request=request, format=format),
    })


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PatientRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.filter(role='patient')
    serializer_class = PatientRegisterSerializer


class DoctorRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.filter(role='doctor')
    serializer_class = DoctorRegisterSerializer


class PatientMedicalRecordList(generics.ListAPIView):
    serializer_class = MedicalRecordSerializer

    def get_queryset(self):
        patient_id = self.kwargs.get("patient_id")  # Get patient_id from URL
        return MedicalRecord.objects.filter(patient=patient_id)


class MedicalRecordList(generics.ListCreateAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(patient=self.request.user)


class MedicalRecordDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class AppointmentList(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class AppointmentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class PatientAppointmentList(generics.ListAPIView):
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        patient_id = self.kwargs.get("patient_id")  # Get patient_id from URL
        return Appointment.objects.filter(patient=patient_id)


class DoctorAppointmentList(generics.ListAPIView):
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        doctor_id = self.kwargs.get("doctor_id")  # Get patient_id from URL
        return Appointment.objects.filter(doctor=doctor_id)


class DoctorSlotList(generics.ListCreateAPIView):
    queryset = DoctorSlot.objects.all()
    serializer_class = DoctorSlotSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(doctor=self.request.user)


class DoctorSlotDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = DoctorSlot.objects.all()
    serializer_class = DoctorSlotSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class DoctorDoctorSlotList(generics.ListAPIView):
    serializer_class = DoctorSlotSerializer

    def get_queryset(self):
        doctor_id = self.kwargs.get("doctor_id")  # Get patient_id from URL
        return DoctorSlot.objects.filter(doctor=doctor_id)
