# Generated by Django 4.2.4 on 2023-12-01 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('study_abroad_app', '0006_remove_program_status_application_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='status',
        ),
    ]
