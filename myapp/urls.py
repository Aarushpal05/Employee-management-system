from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.user_login, name='login'),
    path('createemployee', views.create_employee, name='create_employee'),
    path('employeelist', views.employee_list, name='employee_list'),
    path('logout/', views.user_logout, name='logout'),
    path('updateemployee/<int:id>/', views.update_employee, name='update_employee'),
    path('deleteemployee/<int:id>/',views.delete_employee,name="delete_employee"),

]