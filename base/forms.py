from django import forms
from .models import Employee, Training

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ["id", "employee_number", "last_name", "first_name", "talent_segment",
                  "role", "management_level", "home_office", "mail", "team"]

class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ["name", "date"]
