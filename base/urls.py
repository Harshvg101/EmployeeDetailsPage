from django.contrib import admin
from django.urls import path, include
from .views import authView, home, employee_detail, update_employee, add_employee

app_name = "base"  # Add this line to define a namespace

urlpatterns = [
    path("", home, name="home"),
    path('signup/', authView, name='authView'),
    path("accounts/", include("django.contrib.auth.urls")),
    path("employee/add/", add_employee, name="add_employee"),
    path("employee/<str:employee_id>/", employee_detail, name="employee_detail"),
    path("employee/<str:employee_id>/update/", update_employee, name="update_employee"),
]


# from django.urls import path
# from .views import home, employee_detail, update_employee, add_employee
#
# urlpatterns = [
#     path('', home, name='home'),
#     path('employee/add/', add_employee, name='add_employee'),
#     path('employee/<str:employee_id>/', employee_detail, name='employee_detail'),
#
#     path('employee/<str:employee_id>/update/', update_employee, name='update_employee'),
# ]
