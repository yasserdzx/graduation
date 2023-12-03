# study_abroad_app/urls.py
from django.urls import path
from .views import home , apply , signup , logout_view , login_view , check_uploaded_files , download_application_form , delete_application 
from study_abroad_app.views import download_passport_upload
from django.contrib.auth.views import LoginView
from study_abroad_app import views
from .views import success_page
urlpatterns = [

    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('apply/', apply, name='apply'),
    path('logout/', logout_view, name='logout'),
    path('apply/<int:program_id>/', apply, name='apply_program'),
    path('check_files/', check_uploaded_files, name='check_files'),
    path('download_application_form/', download_application_form, name='download_application_form'),
    path('download_passport_upload/<int:application_id>/', download_passport_upload, name='download_passport_upload'),
    path('delete_application/<int:application_id>/', delete_application, name='delete_application'),
    path('edit_application/<int:application_id>/', views.edit_application, name='edit_application'),
    path('guide/', views.guide, name='guide'), 
    path('aboutus/', views.aboutus, name='aboutus'), 
    path('success/', success_page, name='success_page'),


]
