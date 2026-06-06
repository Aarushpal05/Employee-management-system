
from django.shortcuts import render, redirect
from .models import *
from .form import EmployeeForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def create_employee(request):

    if request.method == 'POST':

        form = EmployeeForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('employee_list')

    else:

        form = EmployeeForm()

    return render(request, 'employee_form.html', {
        'form': form
    })

def employee_list(request):
    employees = Employee.objects.all()

    return render(request, 'view_employee.html', {
        'employees': employees
    })

def update_employee(request, id):

    employee = Employee.objects.get(id=id)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)



        if form.is_valid():
            form.save()
            return redirect('create_employee')

    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'employee_form.html', {'form': form})


# DELETE EMPLOYEE
def delete_employee(request, id):

    employee = Employee.objects.get(id=id)

    employee.delete()

    return redirect('employee_list')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('create_employee')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

