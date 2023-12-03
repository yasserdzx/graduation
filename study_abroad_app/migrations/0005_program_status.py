# Generated by Django 4.2.4 on 2023-12-01 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_abroad_app', '0004_application_signed_form_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='status',
            field=models.CharField(choices=[('submitted', 'Submitted'), ('under_review', 'Under Review'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='submitted', max_length=20),
        ),
    ]
