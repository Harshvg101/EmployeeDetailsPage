from django.db import models

class Employee(models.Model):
    id = models.CharField(max_length=50, primary_key=True)  # Enterprise ID
    employee_number = models.CharField(max_length=20, unique=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    talent_segment = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=100)
    management_level = models.IntegerField()
    home_office = models.CharField(max_length=100)
    mail = models.EmailField(unique=True)
    team = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.id

class Training(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="trainings")
    name = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.date})"
