# study_abroad_project/urls.py
from django.contrib import admin
from django.urls import path, include
from study_abroad_app.views import download_signed_form , download_passport_upload , download_certificate_upload
from study_abroad_app.views import apply

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('study_abroad_app.urls')),
    path('download_signed_form/<int:application_id>/', download_signed_form, name='download_signed_form'),
    path('download_passport_upload/<int:application_id>/', download_passport_upload, name='download_passport_upload'),
    path('download_certificate_upload/<int:application_id>/', download_certificate_upload, name='download_certificate_upload'),
    
]

