# Generated by Django 4.2.4 on 2023-11-30 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_abroad_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='program',
        ),
        migrations.RemoveField(
            model_name='application',
            name='user',
        ),
        migrations.AddField(
            model_name='application',
            name='certificate_upload',
            field=models.FileField(default='not uploaded', upload_to='certificate_uploads/'),
        ),
        migrations.AddField(
            model_name='application',
            name='date_of_birth',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AddField(
            model_name='application',
            name='first_name',
            field=models.CharField(default='John', max_length=255),
        ),
        migrations.AddField(
            model_name='application',
            name='last_name',
            field=models.CharField(default='John', max_length=255),
        ),
        migrations.AddField(
            model_name='application',
            name='passport_number',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AddField(
            model_name='application',
            name='passport_upload',
            field=models.FileField(default='not uploaded', upload_to='passport_uploads/'),
        ),
        migrations.AlterField(
            model_name='application',
            name='documents',
            field=models.FileField(upload_to='application_documents/'),
        ),
    ]
