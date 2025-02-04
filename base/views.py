from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
from .models import Employee, Training
from .forms import EmployeeForm, TrainingForm
from django.contrib.auth.forms import UserCreationForm


# Sample Employee Data (Replace with actual database model later)
EMPLOYEES = [
    {"id": "minato.mirai", "employee_number": "666677", "last_name": "mirai", "first_name": "111",
     "talent_segment": "Engin", "role": "Engineering Services Analyst", "management_level": "8",
     "home_office": "OsakaAQA", "mail": "minato.mirai@acn.com", "team": "Cloud",
     "training": [
         {"name": "Accenture Connected Technology Solution(ACTS) Trai", "date": "1990-01-1"},
         {"name": "ProjectCRT - Internal Training for AWS Solution Ar", "date": "1995-06-5"},
         {"name": "Accenture Connected Technology Solution(ACTS) Trai", "date": "2025-01-1"},
     ]},
]

def is_admin(user):
    return user.is_staff  # Only staff (admins) can edit


@login_required
@user_passes_test(is_admin)
def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("base:home")  # Redirect to home page after adding
    else:
        form = EmployeeForm()

    return render(request, "add_employee.html", {"form": form})

@login_required
def home(request):
    query = request.GET.get("q", "")
    filtered_employees = [emp for emp in EMPLOYEES if query.lower() in emp["id"].lower()]

    # Pagination
    paginator = Paginator(filtered_employees, 5)  # Show 5 employees per page
    page_number = request.GET.get("page")
    employees = paginator.get_page(page_number)

    return render(request, "home.html", {"employees": employees})

def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})

@login_required
def employee_detail(request, employee_id):
    employee = next((emp for emp in EMPLOYEES if emp["id"] == employee_id), None)
    if not employee:
        return render(request, "404.html")  # Handle employee not found

    return render(request, "employee_detail.html", {"employee": employee, "is_admin": request.user.is_staff})


@user_passes_test(is_admin)
def update_employee(request, employee_id):
    # Only admin users can access this view
    employee = next((emp for emp in EMPLOYEES if emp["id"] == employee_id), None)
    if not employee:
        return render(request, "404.html")

    if request.method == "POST":
        employee["role"] = request.POST.get("role", employee["role"])
        employee["home_office"] = request.POST.get("home_office", employee["home_office"])
        # You can add more fields to update

    return render(request, "update_employee.html", {"employee": employee})
