from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
from .models import Employee, Training
from .forms import EmployeeForm, TrainingForm
from django.contrib.auth.forms import UserCreationForm

def is_admin(user):
    return user.is_staff  # Only staff (admins) can edit

@login_required
def home(request):
    query = request.GET.get("q", "")
    employees = Employee.objects.filter(id__icontains=query) if query else Employee.objects.all()

    paginator = Paginator(employees, 10)  # Show 10 employees per page
    page_number = request.GET.get("page")
    employees = paginator.get_page(page_number)

    return render(request, "home.html", {"employees": employees, "is_admin": request.user.is_staff})

@login_required
def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    return render(request, "employee_detail.html", {"employee": employee, "is_admin": request.user.is_staff})

@login_required
@user_passes_test(is_admin)
def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("base:home")
    else:
        form = EmployeeForm()

    return render(request, "add_employee.html", {"form": form})

@login_required
@user_passes_test(is_admin)
def update_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect("base:employee_detail", employee_id=employee.id)
    else:
        form = EmployeeForm(instance=employee)

    return render(request, "update_employee.html", {"form": form, "employee": employee})

def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("base:login")
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})
