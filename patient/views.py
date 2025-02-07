from patient.models import MedicalRecord
from patient.serializers import MedicalRecordSerializer
from patient.serializers import UserSerializer, PatientRegisterSerializer, DoctorRegisterSerializer
from patient.permissions import IsOwnerOrReadOnly
from rest_framework import permissions
from rest_framework import generics
from patient.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'records': reverse('record-list', request=request, format=format)
    })


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PatientRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.filter(user_type='patient')
    serializer_class = PatientRegisterSerializer


class DoctorRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.filter(user_type='doctor')
    serializer_class = DoctorRegisterSerializer

# Create your views here.


# class MedicalRecordList(generics.ListCreateAPIView):
#     serializer_class = MedicalRecordSerializer

#     def get_queryset(self):
#         patient_id = self.kwargs.get("patient_id")  # Get patient_id from URL
#         return MedicalRecord.objects.filter(patient=patient_id)
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
