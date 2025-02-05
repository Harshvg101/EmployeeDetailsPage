from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Project(models.Model):
    name = models.CharField(max_length=255)
    account_name = models.CharField(max_length=255)
    date = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "M_project"
        verbose_name_plural = "M_projects"


class Skill(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "M_skill"
        verbose_name_plural = "M_skills"


class Team(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "M_team"
        verbose_name_plural = "M_teams"


class Training(models.Model):
    name = models.CharField(max_length=255)
    period_hours = models.PositiveIntegerField(default=0)
    fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    language = models.CharField(max_length=50, default="English")
    date = models.DateTimeField()  # if you want to capture the date/time together

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "M_training"
        verbose_name_plural = "M_trainings"


class Employee(models.Model):
    # Note: In your target “T_employees” the field names differ slightly.
    enterprise_id = models.CharField(max_length=255, unique=True, default="default_enterprise_id")
    employee_number = models.CharField(max_length=50, default="EMP0001")
    first_name = models.CharField(max_length=100, default="John")
    last_name = models.CharField(max_length=100, default="Doe")
    talent_segment = models.CharField(max_length=100, default="General")
    role = models.CharField(max_length=100, default="Employee")
    management_level = models.IntegerField(default=1)
    home_office = models.CharField(max_length=100, default="Headquarters")
    mail_address = models.EmailField(unique=True, default="default@example.com")
    teams = models.ManyToManyField(Team, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.enterprise_id}"

    class Meta:
        verbose_name = "T_employee"
        verbose_name_plural = "T_employees"

class Background(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    company = models.CharField(max_length=50)
    hire_date = models.DateTimeField(
        help_text="The date and time the employee was hired."
    )
    retire_date = models.DateTimeField(
        help_text="The date and time the employee retired."
    )
    experience = models.TextField(help_text="Employee experience details.")
    # If you want the admin to let you enter the created_at manually, do NOT use auto_now_add.
    created_at = models.DateTimeField(default=timezone.now, help_text="Record creation date.")

    def __str__(self):
        return f"{self.employee} - {self.company}"

    class Meta:
        verbose_name = "T_background"
        verbose_name_plural = "T_backgrounds"


class ProjectHistory(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assign_date = models.DateField()
    release_date = models.DateField()

    def __str__(self):
        return f"{self.employee} - {self.project}"

    class Meta:
        verbose_name = "T_project history"
        verbose_name_plural = "T_project historys"


class TrainingHistory(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    attend_date = models.DateField()

    def __str__(self):
        return f"{self.employee} - {self.training}"

    class Meta:
        verbose_name = "T_training history"
        verbose_name_plural = "T_training historys"


class Background(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    company = models.CharField(max_length=50)
    hire_date = models.DateTimeField()
    retire_date = models.DateTimeField()
    experience = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee} - {self.company}"

    class Meta:
        verbose_name = "T_background"
        verbose_name_plural = "T_backgrounds"



class SkillHistory(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    skill = models.ForeignKey('Skill', on_delete=models.CASCADE)
    # “Register Date” can be recorded as a DateTimeField.
    register_date = models.DateTimeField(
        help_text="The date and time when the employee registered for this skill."
    )

    created_at = models.DateTimeField(default=timezone.now, help_text="Record creation date.")

    def __str__(self):
        return f"{self.employee} - {self.skill}"

    class Meta:
        verbose_name = "T_skill history"
        verbose_name_plural = "T_skill historys"

class TrainingHistory(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    training = models.ForeignKey('Training', on_delete=models.CASCADE)
    # “Attend Date” is when the employee attended the training.
    attend_date = models.DateTimeField(
        help_text="The date and time when the employee attended the training."
    )
    # If you wish to have a separate created date field:
    created_at = models.DateTimeField(default=timezone.now, help_text="Record creation date.")

    def __str__(self):
        return f"{self.employee} - {self.training}"

    class Meta:
        verbose_name = "T_training history"
        verbose_name_plural = "T_training historys"


# class Team(models.Model):
#     name = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.name
#
# class Employee(models.Model):
#     enterprise_id = models.CharField(
#         max_length=255,
#         unique=True,
#         default="default_enterprise_id",
#         help_text="A unique identifier for the employee. Default: 'default_enterprise_id'."
#     )
#     employee_number = models.CharField(
#         max_length=50,
#         default="EMP0001",
#         help_text="Employee identification number. Default: 'EMP0001'."
#     )
#     first_name = models.CharField(
#         max_length=100,
#         default="John",
#         help_text="Employee's first name. Default: 'John'."
#     )
#     last_name = models.CharField(
#         max_length=100,
#         default="Doe",
#         help_text="Employee's last name. Default: 'Doe'."
#     )
#     talent_segment = models.CharField(
#         max_length=100,
#         default="General",
#         help_text="The talent segment the employee belongs to. Default: 'General'."
#     )
#     role = models.CharField(
#         max_length=100,
#         default="Employee",
#         help_text="Employee's role within the company. Default: 'Employee'."
#     )
#     management_level = models.IntegerField(
#         default=1,
#         help_text="The management level of the employee. Default: 1."
#     )
#     home_office = models.CharField(
#         max_length=100,
#         default="Headquarters",
#         help_text="The home office location of the employee. Default: 'Headquarters'."
#     )
#     mail_address = models.EmailField(
#         unique=True,
#         default="default@example.com",
#         help_text="Employee's email address. Default: 'default@example.com'."
#     )
#     teams = models.ManyToManyField(
#         'Team',
#         blank=True,
#         help_text="Teams the employee belongs to. (No default value is set for ManyToMany fields.)"
#     )
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name} - {self.enterprise_id}"
#
# class Project(models.Model):
#     name = models.CharField(max_length=255)
#     account_name = models.CharField(max_length=255)
#     date = models.DateField()
#
#     def __str__(self):
#         return self.name
#
# class Skill(models.Model):
#     name = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.name
#
# class Training(models.Model):
#     name = models.CharField(max_length=255)
#     date = models.DateField()  # New field added
#     period_hours = models.PositiveIntegerField()
#     fee = models.DecimalField(max_digits=10, decimal_places=2)
#     language = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.name
#
# class TrainingHistory(models.Model):
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     training = models.ForeignKey(Training, on_delete=models.CASCADE)
#     attend_date = models.DateField()
#
#     def __str__(self):
#         return f"{self.employee} - {self.training}"
#
# class ProjectHistory(models.Model):
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     assign_date = models.DateField()
#     release_date = models.DateField()
#
#     def __str__(self):
#         return f"{self.employee} - {self.project}"
