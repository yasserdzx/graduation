# study_abroad_app/models.py
from django.db import models
from django.contrib.auth.models import User

class Program(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    application_deadline = models.DateField()
    country = models.CharField(max_length=50)


    def __str__(self):
        return self.title
class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , default=1)
    first_name = models.CharField(max_length=255 ,  default='John')
    last_name = models.CharField(max_length=255,  default='John')
    passport_number = models.CharField(max_length=20,  default=0000)
    date_of_birth = models.DateField(default='2000-01-01')
    passport_upload = models.FileField(upload_to='passport_uploads/' , default='not uploaded')
    certificate_upload = models.FileField(upload_to='certificate_uploads/', default='not uploaded')
    motivation_statement = models.TextField()  # Add this field
    documents = models.FileField(upload_to='application_documents/')  # Add this field
    signed_form_upload = models.FileField(upload_to='signed_forms/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def get_status_display(self):
        # Handle 'pending' separately or use a default implementation
        if self.status == 'pending':
            return 'Pending'
        return dict(self.STATUS_CHOICES).get(self.status, self.status)

    

    def delete_application(self):
        self.delete()

    def __str__(self):
        return f'{self.user.username} - Application {self.id}'
    

    
