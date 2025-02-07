from django.urls import path
from patient import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.api_root),
    path('create-record/', views.MedicalRecordList.as_view()),
    path("register-patient/", views.PatientRegisterAPIView.as_view()),
    path("user/", views.UserList.as_view(), name='user-list'),
    # path('view-records/<int:pk>/',
    #      views.MedicalRecordDetails.as_view()),
    path('view-records/all/',
         views.MedicalRecordList.as_view(), name='record-list'),
    path('update-record/<int:pk>/',
         views.MedicalRecordDetails.as_view()),
    path('delete-record/<int:pk>/',
         views.MedicalRecordDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
