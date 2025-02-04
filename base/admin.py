from django.contrib import admin
from .models import Employee, Training

# class TrainingInline(admin.TabularInline):
#     model = Training
#     extra = 1  # Allows adding training records while editing employees

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id", "employee_number", "last_name", "first_name", "role", "home_office")
    search_fields = ("id", "employee_number", "last_name", "first_name", "role", "home_office")
    list_filter = ("role", "home_office")
    # inlines = [TrainingInline]  # Enables adding training records from the employee form


# Prevent duplicate registration
if not admin.site.is_registered(Employee):
    admin.site.register(Employee, EmployeeAdmin)
if not admin.site.is_registered(Training):
    admin.site.register(Training)
#
#
# admin.site.register(Employee, EmployeeAdmin)
# admin.site.register(Training)
