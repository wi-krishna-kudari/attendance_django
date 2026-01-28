from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.list_students),
    path('students/create/', views.create_student),
    path('students/<int:id>/', views.get_student_details),
]