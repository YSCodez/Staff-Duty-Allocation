from. import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('index1/', views.index1),
    path('AdminSignIn/', views.AdminSignIn),
    path('AdminLogin/', views.AdminLogin),
    path('Emppage/', views.emppage),
    path('Addemploy/', views.addemploy),
    path('taskallocation/', views.taskallocation),
    path('404Notfound/', views.Notfound),
    path('blank/', views.blank),
    path('Confirmation/', views.Conformation),
    path('AssignedEmTask/', views.assignedTaskem),
    path('AssignTask/', views.AssignTask),
    path('employeeComplainPage/',views.employeeComplainPage),
    path('complainRegistered/', views.complainRegistered),
    path('SingUp/', views.UserRegister),
    path('UseradminRegister/', views.UseradminRegister),
    path('userLogin/', views.handleLogin),
    path('AdminlogVerif/', views.handleAdminLogin),
    path('logout/', views.handleadminLogout),
    path('usrlogout/', views.handleuserLogout),
    path('registerTask/', views.getTask),
    path('allocShift/', views.allocShift),
    path('registerFeed/', views.getFeed),
    path('delete_Feed/<event_id>', views.delete_Feed, name= 'delete-event'),
    path('delete_task/<event_id>', views.emptaskdelete, name= 'delete-task'),
    path('data/', views.adminfeed),
    path('delete/', views.delete),
    path('allocateshit/', views.allocShit),
]