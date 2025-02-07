from django.urls import path
from patient import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.api_root),
    path("user/", views.UserList.as_view(), name='user-list'),
    path('create-record/', views.MedicalRecordList.as_view(), name='record-list'),
    path('view-records/<int:patient_id>/',
         views.PatientMedicalRecordList.as_view()),
    path('update-record/<int:pk>/',
         views.MedicalRecordDetails.as_view()),
    path('delete-record/<int:pk>/',
         views.MedicalRecordDetails.as_view()),
    path('create-appointment/', views.AppointmentList.as_view(), name='appointment-list'),
    path('view-appointments/<int:patient_id>/',
         views.PatientAppointmentList.as_view()),
    path('view-doctor-appointments/<int:doctor_id>/',
         views.DoctorAppointmentList.as_view()),
    path('update-appointment/<int:pk>/', views.AppointmentDetails.as_view()),
    path('delete-appointment/<int:pk>/', views.AppointmentDetails.as_view()),
    path('create-slot/', views.DoctorSlotList.as_view(), name='slot-list'),
    path('view-slots/<int:doctor_id>/', views.DoctorDoctorSlotList.as_view()),
    path('update-slot/<int:pk>/', views.DoctorSlotDetails.as_view()),
    path('delete-slot/<int:pk>/', views.DoctorSlotDetails.as_view()),
    path("register-patient/", views.PatientRegisterAPIView.as_view()),
    path('update-patient/<int:pk>/', views.PatientRegisterAPIView.as_view()),
    path('delete-patient/<int:pk>/', views.PatientRegisterAPIView.as_view()),
    path("register-doctor/", views.DoctorRegisterAPIView.as_view()),
    path('update-doctor/<int:pk>/', views.DoctorRegisterAPIView.as_view()),
    path('delete-doctor/<int:pk>/', views.DoctorRegisterAPIView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
