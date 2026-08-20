from django.urls import path

from . import views

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='school-list'),
    path('schools/add/', views.SchoolCreateView.as_view(), name='school-add'),
    path('schools/<int:pk>/edit/', views.SchoolUpdateView.as_view(), name='school-edit'),
    path('schools/<int:pk>/delete/', views.SchoolDeleteView.as_view(), name='school-delete'),

    path('students/', views.StudentListView.as_view(), name='student-list'),
    path('students/add/', views.StudentCreateView.as_view(), name='student-add'),
    path('students/<int:pk>/edit/', views.StudentUpdateView.as_view(), name='student-edit'),
    path('students/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student-delete'),
]
