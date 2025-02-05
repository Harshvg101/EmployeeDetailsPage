from django.contrib import admin
from .models import (
    Employee,
    Project,
    Skill,
    Training,
    ProjectHistory,
    Team,
    Background,
    SkillHistory,
    TrainingHistory,
)
# Customize Django Admin interface
admin.site.site_header = "Employee Management System"
admin.site.site_title = "EMS Admin"
admin.site.index_title = "Admin Dashboard"

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('enterprise_id', 'first_name', 'last_name', 'role', 'home_office', 'mail_address')
    search_fields = ('enterprise_id', 'first_name', 'last_name', 'role', 'mail_address')
    list_filter = ('role', 'home_office')
    filter_horizontal = ('teams',)

    # Restrict deletion to superusers only
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    # Allow HR group to edit, but restrict others
    def has_change_permission(self, request, obj=None):
        if request.user.groups.filter(name="HR").exists():
            return True  # Allow HR group to edit
        return request.user.is_superuser  # Allow superusers

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'account_name', 'date')
    search_fields = ('name', 'account_name')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ('name', 'period_hours', 'fee', 'language')
    search_fields = ('name', 'language')

# @admin.register(TrainingHistory)
# class TrainingHistoryAdmin(admin.ModelAdmin):
#     list_display = ('employee', 'training', 'attend_date')
#     list_filter = ('training', 'attend_date')

@admin.register(ProjectHistory)
class ProjectHistoryAdmin(admin.ModelAdmin):
    list_display = ('employee', 'project', 'assign_date', 'release_date')
    list_filter = ('assign_date', 'release_date')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Background)
class BackgroundAdmin(admin.ModelAdmin):
    """
    Admin customization for T_backgrounds.
    Displays:
      - Employee and Company on the first section.
      - Hire and Retire dates together.
      - Experience details along with the creation timestamp.
    """
    fieldsets = (
        (None, {
            'fields': ('employee', 'company')
        }),
        ('Dates', {
            'fields': (('hire_date', 'retire_date'),)
        }),
        ('Additional', {
            'fields': ('experience', 'created_at'),
        }),
    )
    list_display = ('employee', 'company', 'hire_date', 'retire_date')


@admin.register(SkillHistory)
class SkillHistoryAdmin(admin.ModelAdmin):
    """
    Admin customization for T_skill historys.
    Displays:
      - Employee and Skill together.
      - Register date and the record’s created timestamp.
    """
    fieldsets = (
        (None, {
            'fields': (('employee', 'skill'),)
        }),
        ('Dates', {
            'fields': (('register_date', 'created_at'),)
        }),
    )
    list_display = ('employee', 'skill', 'register_date')


@admin.register(TrainingHistory)
class TrainingHistoryAdmin(admin.ModelAdmin):
    """
    Admin customization for T_training historys.
    Displays:
      - Employee and Training together.
      - Attend date along with the record creation date.
    """
    fieldsets = (
        (None, {
            'fields': (('employee', 'training'),)
        }),
        ('Dates', {
            'fields': (('attend_date', 'created_at'),)
        }),
    )
    list_display = ('employee', 'training', 'attend_date')
