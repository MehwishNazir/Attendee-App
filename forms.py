# attendance_app/forms.py

from django import forms

from . import models
from .models import Subject, Attendance


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name']  # Fields you want to include in the form


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['subject','date', 'is_present']  # Fields you want to include in the form
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})  # You can remove this line
        }
