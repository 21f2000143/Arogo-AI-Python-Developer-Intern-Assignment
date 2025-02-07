from django.urls import path
from clini360 import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('create-record/', views.MedicalRecordDetails.as_view()),
    path("register-patient/", views.RegisterUserView.as_view()),
    path("login/", views.LoginView.as_view()),
    path('view-records/<int:patient_id>/',
         views.MedicalRecordDetails.as_view()),
    path('update-record/<int:record_id>/',
         views.MedicalRecordDetails.as_view()),
    path('delete-record/<int:record_id>/',
         views.MedicalRecordDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
