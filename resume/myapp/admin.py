from django.contrib import admin
from .models import Resume

@admin.register(Resume)
class ResumeModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'name', 'dob', 'gender', 'locality', 'city', 'pin', 'state', 'mobile', 'job_city', 'profile_image', 'my_file']
 labels = {'name': 'Full Name', 'dob': 'Date of Birth', 'pin': 'Pin Code', 'mobile': 'Mobile No.', 'email': 'Email ID',
           'profile_image': 'Profile Image', 'my_file': 'Document'}