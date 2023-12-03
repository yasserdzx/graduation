# study_abroad_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Program , Application
from .forms import ApplicationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login , authenticate
from .forms import SignUpForm, ApplicationForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse

@login_required
def home(request):
    programs = Program.objects.all()
    return render(request, 'study_abroad_app/home.html', {'programs': programs})

@login_required
def check_uploaded_files(request):
    user_applications = Application.objects.filter(user=request.user)
    return render(request, 'study_abroad_app/check_files.html', {'user_applications': user_applications})


def guide(request):
    return render(request , 'study_abroad_app/guide.html')


def aboutus(request):
    return render(request , 'study_abroad_app/aboutus.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'study_abroad_app/signup.html', {'form': form})

def download_application_form(request):
    # Add logic to generate or serve the application form for download
    # For example, you can create a static PDF file and provide a link to download it
    file_path = 'C:/Users/user/Desktop/grad-with program/study_abroad_project/study_abroad_app/ApplicationForm.pdf'
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename=application_form.pdf'
        return response


def delete_application(request, application_id):
    application = get_object_or_404(Application, id=application_id, user=request.user)

    if request.method == 'POST':
        application.delete_application()
        return redirect('check_files')

    return render(request, 'study_abroad_app/delete_application.html', {'application': application})


@login_required
def apply(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user  # Set the user
            application.status = 'pending'  # Set the status to a default value
            application.save()
            return redirect(reverse('success_page'))
        else:
            print(form.errors)  # Print form errors to the console for debugging
    else:
        form = ApplicationForm()

    return render(request, 'study_abroad_app/apply.html', {'form': form, 'programs': Program.objects.all()})

def success_page(request):
    return render(request, 'study_abroad_app/success_page.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Log the user in
            user = form.get_user()
            login(request, user)
            # Redirect to a success page or home
            return redirect('home')
    else:
        form = AuthenticationForm()
    
    return render(request, 'study_abroad_app/login.html', {'form': form})


def edit_application(request, application_id):
    application = get_object_or_404(Application, id=application_id)

    if request.method == 'POST':
        form = ApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('check_files')
    else:
        form = ApplicationForm(instance=application)

    return render(request, 'study_abroad_app/edit_application.html', {'form': form, 'application': application})
def download_signed_form(request, application_id):
    application = get_object_or_404(Application, id=application_id)
    if application.signed_form_upload:
        with open(application.signed_form_upload.path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'inline; filename={application.signed_form_upload.name}'
            return response
    else:
        # Handle the case where the signed form is not found
        return HttpResponse("Signed form not found.", status=404)

def download_passport_upload(request, application_id):
    application = get_object_or_404(Application, id=application_id)
    if application.passport_upload:
        with open(application.passport_upload.path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='image/png')  # Adjust content type based on your file type
            response['Content-Disposition'] = f'inline; filename={application.passport_upload.name}'
            return response
    else:
        # Handle the case where the passport upload is not found
        return HttpResponse("Passport upload not found.", status=404)
    
def download_certificate_upload(request, application_id):
    application = get_object_or_404(Application, id=application_id)
    if application.certificate_upload:
        with open(application.certificate_upload.path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='image/png')  # Adjust content type based on your file type
            response['Content-Disposition'] = f'inline; filename={application.certificate_upload.name}'
            return response
    else:
        # Handle the case where the passport upload is not found
        return HttpResponse("certeficate upload not found.", status=404)
def logout_view(request):
    logout(request)
    return redirect('home')



