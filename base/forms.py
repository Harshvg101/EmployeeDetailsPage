from django import forms
from .models import Employee, Training

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            "enterprise_id",
            "employee_number",
            "last_name",
            "first_name",
            "talent_segment",
            "role",
            "management_level",
            "home_office",
            "mail_address",  # Changed from "mail" to "mail_address"
            "teams",         # Changed from "team" to "teams"
        ]

class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ["name", "period_hours", "fee", "language", "date"]
